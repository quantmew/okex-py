
from typing import Union, Optional, Iterable
from enum import Enum

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .ccytype import CcyType

class TdMode(Enum):
    # 保证金模式
    ISOLATED = "isolated"
    CROSS = "cross"
    # 非保证金模式
    CASH = "cash"

class PosSide(Enum):
    LONG = "long"
    SHORT = "short"

class OrderType(Enum):
    # 市价单
    MARKET = "market"
    # 限价单
    LIMIT = "limit"
    # 只做maker单
    POST_ONLY = "post_only"
    # 全部成交或立即取消
    FOK = "fok"
    # 立即成交并取消剩余
    IOC = "ioc"

class TradeAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def order(self, instId:str,
            tdMode: Union[TdMode, str],
            ordType: Union[OrderType, str],
            sz: Union[float, int, str],
            ccy: Optional[Union[CcyType, str]]=None,
            clOrdId: Optional[str]=None,
            tag: Optional[str]=None,
            posSide: Optional[Union[PosSide, str]]=None,
            px: Optional[Union[float, int, str]]=None,
            reduceOnly: Optional[Union[str, bool]]=None
            ):
        params = {}
        if instId is not None:
            params['instId'] = str(instId)
        if tdMode is not None:
            params['tdMode'] = enum_to_str(tdMode)
        if ordType is not None:
            params['ordType'] = enum_to_str(ordType)
        if sz is not None:
            params['sz'] = str(abs(sz))
            if sz >= 0:
                params['side'] = 'buy'
            else:
                params['side'] = 'sell'
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)
        if clOrdId is not None:
            params['clOrdId'] = str(clOrdId)
        if tag is not None:
            params['tag'] = str(tag)
        if posSide is not None:
            params['posSide'] = enum_to_str(posSide)
        if px is not None:
            params['px'] = str(px)
        if reduceOnly is not None:
            if isinstance(reduceOnly, bool):
                if reduceOnly:
                    params['reduceOnly'] = 'true'
                else:
                    params['reduceOnly'] = 'false'
            else:
                params['reduceOnly'] = str(reduceOnly)
        data = self._request_with_params(POST, ORDER, params)["data"]

        return data

    def get_order(self, instId:str, ordId:Optional[str]=None, clOrdId:Optional[str]=None):
        params = {}
        if instId is not None:
            params['instId'] = str(instId)
        if ordId is not None:
            params['ordId'] = str(ordId)
        if clOrdId is not None:
            params['clOrdId'] = str(clOrdId)
        
        data = self._request_with_params(GET, ORDER, params)["data"]

        return data