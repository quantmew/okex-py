
import asyncio
from typing import Callable, Dict, List, Optional, Union
import websocket
import datetime
import json

from .consts import WS_PUBLIC_TEST_URL, WS_PRIVATE_TEST_URL, WS_PUBLIC_URL, WS_PRIVATE_URL
from .utils import get_timestamp, get_local_timestamp, signature, to_list, enum_to_str
from .insttype import InstType


PUBLIC_CHANNELS = ["instruments", "tickers", "open-interest",
                    "candle1Y",
                    "candle6M", "candle3M", "candle1M",
                    "candle1W",
                    "candle1D", "candle2D", "candle3D", "candle5D",
                    "candle12H", "candle6H", "candle4H", "candle2H", "candle1H",
                    "candle30m", "candle15m", "candle5m", "candle3m", "candle1m",
                    "candle1Yutc", "candle3Mutc", "candle1Mutc", "candle1Wutc", "candle1Dutc", "candle2Dutc", "candle3Dutc", "candle5Dutc", "candle12Hutc", "candle6Hutc",
                    "trades", "estimated-price", "mark-price", 
                    "mark-price-candle1Y", "mark-price-candle6M", "mark-price-candle3M", "mark-price-candle1M", "mark-price-candle1W",
                    "mark-price-candle1D", "mark-price-candle2D", "mark-price-candle3D", "mark-price-candle5D", "mark-price-candle12H",
                    "mark-price-candle6H", "mark-price-candle4H", "mark-price-candle2H", "mark-price-candle1H", "mark-price-candle30m",
                    "mark-price-candle15m", "mark-price-candle5m", "mark-price-candle3m", "mark-price-candle1m", "mark-price-candle1Yutc",
                    "mark-price-candle3Mutc", "mark-price-candle1Mutc", "mark-price-candle1Wutc", "mark-price-candle1Dutc", "mark-price-candle2Dutc",
                    "mark-price-candle3Dutc", "mark-price-candle5Dutc", "mark-price-candle12Hutc", "mark-price-candle6Hutc", 
                    "price-limit", 
                    "books", "books5", "books-l2-tbt", "books50-l2-tbt",
                    "opt-summary", "funding-rate",
                    "index-candle1Y", "index-candle6M", "index-candle3M", "index-candle1M", "index-candle1W", "index-candle1D", "index-candle2D", "index-candle3D",
                    "index-candle5D", "index-candle12H", "index-candle6H", "index-candle4H", "index -candle2H", "index-candle1H", "index-candle30m", "index-candle15m",
                    "index-candle5m", "index-candle3m", "index-candle1m", "index-candle1Yutc", "index-candle3Mutc", "index-candle1Mutc", "index-candle1Wutc", "index-candle1Dutc",
                    "index-candle2Dutc", "index-candle3Dutc", "index-candle5Dutc", "index-candle12Hutc", "index-candle6Hutc",
                    "index-tickers", "status"
                    ]

PRIVATE_CHANNELS = ["account", "positions", "balance_and_position", "orders", "orders-algo", "algo-advance", "liquidation-warning", "account-greeks"]

def is_private_channel(channel: str) -> bool:
    return channel in PRIVATE_CHANNELS

class AccountInfo(object):
    def __init__(self, apiKey: str, passphrase: str) -> None:
        self.apiKey = apiKey
        self.passphrase = passphrase

class Channel(object):
    def __init__(self, name: str,
                instType: Optional[Union[str, InstType]] = None,
                uly: Optional[str] = None,
                instId: Optional[str] = None) -> None:
        self.name = name
        self.instType = enum_to_str(instType)
        self.uly = uly
        self.instId = instId

    def to_dict(self) -> Dict[str, str]:
        ret = {
            "channel": self.name,
        }
        if self.instType is not None:
            ret["inst_type"] = self.instType
        if self.uly is not None:
            ret["uly"] = self.uly
        if self.instId is not None:
            ret["inst_id"] = self.instId
        return ret

class WebSocketAPI(object):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False):
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time
        self.test = test

        if test:
            self.public_api_url = WS_PUBLIC_TEST_URL
            self.private_api_url = WS_PRIVATE_TEST_URL
        else:
            self.public_api_url = WS_PUBLIC_URL
            self.private_api_url = WS_PRIVATE_URL

        self.public_websocket = None
        self.private_websocket = None

    async def connect_public(self) -> None:
        self.public_websocket = websocket.WebSocket()
        self.public_websocket.connect(self.public_api_url)
    
    async def connect_private(self) -> None:
        self.private_websocket = websocket.WebSocket()
        self.private_websocket.connect(self.private_api_url)
        await self.login()

    async def disconnect_public(self) -> None:
        if self.public_websocket is not None:
            self.public_websocket.close()
            self.public_websocket = None
    
    async def disconnect_private(self) -> None:
        if self.private_websocket is not None:
            self.private_websocket.close()
            self.private_websocket = None

    async def disconnect(self) -> None:
        await self.disconnect_public()
        await self.disconnect_private()

    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    def ping(self) -> None:
        if self.private_websocket is not None:
            self.private_websocket.send("ping")
        if self.public_websocket is not None:
            self.public_websocket.send("ping")

    def login_params(self, accounts: List[AccountInfo]):
        timestamp = str(get_local_timestamp())
        sign = signature(timestamp, 'GET', '/users/self/verify', '', self.API_SECRET_KEY)
        sign = sign.decode('utf-8')
        params = {
            "op": "login",
            "args":[]
        }

        for account in accounts:
            params['args'].append({
                "apiKey": account.apiKey,
                "passphrase": account.passphrase,
                "timestamp": timestamp,
                "sign" :sign
                }
            )
        return params

    async def login(self, is_public=True):
        params = self.login_params([AccountInfo(self.API_KEY, self.PASSPHRASE)])
        self.private_websocket.send(json.dumps(params))
        ret = self.private_websocket.recv()
        retObj = json.loads(ret)
        if retObj['code'] == "0":
            print("login success")
        else:
            print("login failed")

    def subscribe_params(self, channels: Union[List[Channel], Channel]):
        channel_list = to_list(channels)
        params = {
            "op":"subscribe",
            "args":[]
        }

        for channel in channel_list:
            params['args'].append(channel.to_dict())
        return params

    async def subscribe_public(self, channels: Union[List[Channel], Channel]):
        if self.public_websocket is None:
            await self.connect_public()

        channel_list = to_list(channels)

        params = self.subscribe_params(channel_list)
        self.public_websocket.send(json.dumps(params))
        ret = self.public_websocket.recv()
        retObj = json.loads(ret)
        print(retObj)
    
    async def subscribe_private(self, channels: Union[List[Channel], Channel]):
        if self.private_websocket is None:
            await self.connect_private()

        channel_list = to_list(channels)

        params = self.subscribe_params(channel_list)
        self.private_websocket.send(json.dumps(params))
        ret = self.private_websocket.recv()
        retObj = json.loads(ret)
        print(retObj)

    async def subscribe(self, channels: Union[List[Channel], Channel]):
        channel_list = to_list(channels)

        public_channels = [channel for channel in channel_list if not is_private_channel(channel.name)]
        private_channels = [channel for channel in channel_list if is_private_channel(channel.name)]

        if len(public_channels) > 0:
            await self.subscribe_public(public_channels)
        if len(private_channels) > 0:
            await self.subscribe_private(private_channels)

    async def unsubscribe_public(self, channels: Union[List[Channel], Channel]):
        channel_list = to_list(channels)

        params = self.subscribe_params(channel_list)
        self.public_websocket.send(json.dumps(params))
        ret = self.public_websocket.recv()
        retObj = json.loads(ret)
        print(retObj)
    
    async def unsubscribe_private(self, channels: Union[List[Channel], Channel]):
        channel_list = to_list(channels)

        params = self.subscribe_params(channel_list)
        self.private_websocket.send(json.dumps(params))
        ret = self.private_websocket.recv()
        retObj = json.loads(ret)
        print(retObj)

    async def unsubscribe(self, channels: Union[List[Channel], Channel]):
        channel_list = to_list(channels)

        public_channels = [channel for channel in channel_list if not is_private_channel(channel.name)]
        private_channels = [channel for channel in channel_list if is_private_channel(channel.name)]

        if len(public_channels) > 0:
            await self.unsubscribe_public(public_channels)
        if len(private_channels) > 0:
            await self.unsubscribe_private(private_channels)