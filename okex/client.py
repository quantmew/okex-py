
import hmac
import base64
from hashlib import sha256
import requests
import datetime
import json
import pandas as pd
from .exceptions import InvalidDataError, ParamsError

from enum import Enum

from typing import Optional


class InstType(Enum):
    # 币币
    SPOT = "SPOT"
    # 永续合约
    SWAP = "SWAP"
    # 交割合约
    FUTURES = "FUTURES"
    # 期权
    OPTION = "OPTION"

'''
指数计价单位
'''
class QuoteCcy(Enum):
    USD = "USD"
    USDT = "USDT"
    BTC = "BTC"

class OrderType(object):
    pass


class MarketOrder(OrderType):
    name = 'market'

    def __init__(self):
        pass

class LimitOrder(OrderType):
    name = 'limit'

    def __init__(self, limit_price):
        self.limit_price = limit_price
    
class PostOnlyOrder(OrderType):
    name = 'post_only'

    def __init__(self):
        pass


class FokOrder(OrderType):
    name = 'fok'

    def __init__(self):
        pass


class IocOrder(OrderType):
    name = 'ioc'

    def __init__(self):
        pass


class OkAPI(object):
    domain = "https://www.okex.com"

    def __init__(self, key, secret_key, passphrase):
        self.key = key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def get_sign(self, timestamp, method, requestPath, body=''):
        content = timestamp + method + requestPath + body
        sha256_bytes = hmac.new(self.secret_key.encode(), content.encode(), digestmod=sha256).digest()
        b64 = base64.b64encode(sha256_bytes).decode()
        return b64

    def get_timestamp(self):
        utcnow = datetime.datetime.utcnow()
        return utcnow.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    def get_header(self, method, url, body=""):
        timestamp = self.get_timestamp()
        return {
            'OK-ACCESS-KEY': self.key,
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-SIGN': self.get_sign(timestamp, method, url, body),
            'OK-ACCESS-PASSPHRASE': self.passphrase
        }

    def get(self, category, method, params=None):
        url = "/api/v5/" + category + "/" + method
        if params is None:
            out = requests.get(self.domain + url,
                               headers=self.get_header("GET", url))
        else:
            out = requests.get(self.domain + url, params=params,
                               headers=self.get_header("GET", url))
        return out.text

    def post(self, category, method, params=None):
        body = json.dumps(params)
        url = "/api/v5/" + category + "/" + method
        headers = self.get_header("POST", url, body)
        headers['Content-Type'] = 'application/json'
        if params is None:
            out = requests.post(self.domain + url, headers=headers)
        else:
            out = requests.post(self.domain + url, data=body, headers=headers)
        return out.text

    def account_position_risk(self):
        out = self.get('account', 'account-position-risk')
        obj = json.loads(out)
        if obj['code'] == '0':
            return obj['data']
        else:
            raise InvalidDataError("")

    def ticker(self, instId: str):
        out = self.get('market', 'ticker', {'instId': instId})
        obj = json.loads(out)
        if obj['code'] == '0':
            return obj['data']
        else:
            raise InvalidDataError("")

    def tickers(self, instType: InstType, uly: Optional[str]=None):
        params = {'instType': str(instType)}
        if uly is not None:
            params['uly'] = uly
        out = self.get('market', 'tickers', params)
        obj = json.loads(out)
        if obj['code'] == '0':
            return obj['data']
        else:
            raise InvalidDataError("")

    def index_tickers(self, quoteCcy: Optional[QuoteCcy]=None, instId: Optional[str]=None):
        pass
    
    def candles(self, instId:str, bar:str='1m', after:Optional[str]=None, before:Optional[str]=None, limit:int=100):
        params = {
                'instId': instId,
                'bar': bar,
                'limit': limit
            }
        if after is not None:
            params['after'] = after

        if before is not None:
            params['before'] = before
    
        out = self.get(
            'market',
            'candles',
            params
        )
        obj = json.loads(out)
        if obj['code'] == '0':
            df = pd.DataFrame(obj['data'], columns=[
                              "ts", "o", "h", "l", "c", "vol", "volCcy"])
            df['ts'] = df['ts'].apply(
                lambda x: datetime.datetime.fromtimestamp(int(x)/1000))
            return df
        else:
            raise InvalidDataError(obj['code'] + ": " + obj['msg'])
    
    def history_candles(self, instId:str, bar:str='1m', after:Optional[str]=None, before:Optional[str]=None, limit:int=100):
        params = {
                'instId': instId,
                'bar': bar,
                'limit': limit
            }
        if after is not None:
            params['after'] = after

        if before is not None:
            params['before'] = before
    
        out = self.get(
            'market',
            'history-candles',
            params
        )
        obj = json.loads(out)
        if obj['code'] == '0':
            df = pd.DataFrame(obj['data'], columns=[
                              "ts", "o", "h", "l", "c", "vol", "volCcy"])
            df['ts'] = df['ts'].apply(
                lambda x: datetime.datetime.fromtimestamp(int(x)/1000))
            return df
        else:
            raise InvalidDataError(obj['code'] + ": " + obj['msg'])

    def order(self, instId, sz: float, posSide: str = 'long', ordType: OrderType = None, tdMode: str = 'cash'):

        if not isinstance(ordType, OrderType):
            raise ParamsError("ordType必须是OrderType类型")
        if sz >= 0:
            order_size = sz
            side = 'buy'
        else:
            order_size = abs(sz)
            side = 'sell'
        out = self.post(
            'trade',
            'order',
            {
                'instId': instId,
                'tdMode': tdMode,
                'side': side,
                'ordType': ordType.name,
                'sz': str(order_size)
            }
        )
        obj = json.loads(out)
        print(obj)
        if obj['code'] == '0':
            return obj['data']
        else:
            raise InvalidDataError(obj['code'] + ": " + obj['msg'])
