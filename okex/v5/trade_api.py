
from typing import Dict, Union, Optional, Iterable
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


class TrgCCY(Enum):
    # 交易货币
    BASE_CCY = "base_ccy"
    # 计价货币
    QUOTE_CCY = "quote_ccy"


class Order(object):
    def __init__(self,
            instId: str,
            tdMode: Union[TdMode, str],
            ordType: Union[OrderType, str],
            sz: Union[float, int, str],
            ccy: Optional[Union[CcyType, str]] = None,
            clOrdId: Optional[str] = None,
            tag: Optional[str] = None,
            posSide: Optional[Union[PosSide, str]] = None,
            reduceOnly: Optional[Union[str, bool]] = None,
            tgtCcy: Optional[Union[TrgCCY, str]] = None
        ) -> None:
        super().__init__()
        self.instId = instId
        self.tdMode = tdMode
        self.ordType = ordType
        self.sz = sz
        self.ccy = ccy
        self.clOrdId = clOrdId
        self.tag = tag
        self.posSide = posSide
        self.reduceOnly = reduceOnly
        self.tgtCcy = tgtCcy
        
class CancelOrder(object):
    def __init__(self, instId: str, ordId: Optional[str] = None, clOrdId: Optional[str] = None) -> None:
        super().__init__()
        self.instId = instId
        self.ordId = ordId
        self.clOrdId = clOrdId

class TradeAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key,
                        passphrase, use_server_time, test, first)

    def order(self, instId: str,
              tdMode: Union[TdMode, str],
              ordType: Union[OrderType, str],
              sz: Union[float, int, str],
              ccy: Optional[Union[CcyType, str]] = None,
              clOrdId: Optional[str] = None,
              tag: Optional[str] = None,
              posSide: Optional[Union[PosSide, str]] = None,
              px: Optional[Union[float, int, str]] = None,
              reduceOnly: Optional[Union[str, bool]] = None
              ) -> Dict:
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

    def batch_orders(self, orders: Union[Order, Iterable[Order]]) -> Dict:
        orders_list = []
        if isinstance(orders, Order):
            orders_list.append(orders)
        else:
            orders_list = orders
        params = []

        for order in orders_list:
            param = {}
            if order.instId is not None:
                param['instId'] = str(order.instId)
            if order.tdMode is not None:
                param['tdMode'] = enum_to_str(order.tdMode)
            if order.ordType is not None:
                param['ordType'] = enum_to_str(order.ordType)
            if order.sz is not None:
                param['sz'] = str(abs(order.sz))
                if order.sz >= 0:
                    param['side'] = 'buy'
                else:
                    param['side'] = 'sell'
            if order.ccy is not None:
                param['ccy'] = enum_to_str(order.ccy)
            if order.clOrdId is not None:
                param['clOrdId'] = str(order.clOrdId)
            if order.tag is not None:
                param['tag'] = str(order.tag)
            if order.posSide is not None:
                param['posSide'] = enum_to_str(order.posSide)

            if order.reduceOnly is not None:
                if isinstance(order.reduceOnly, bool):
                    if order.reduceOnly:
                        param['reduceOnly'] = 'true'
                    else:
                        param['reduceOnly'] = 'false'
                else:
                    param['reduceOnly'] = str(order.reduceOnly)
            if order.tgtCcy is not None:
                param['tgtCcy'] = enum_to_str(order.tgtCcy)
            params.append(param)

        data = self._request_with_params(POST, BATCH_ORDERS, params)["data"]

        return data

    def cancel_order(self, instId: str, ordId: Optional[str] = None, clOrdId: Optional[str] = None):
        params = dict()

        if instId is not None:
            params['instId'] = str(instId)
        if ordId is not None:
            params['ordId'] = str(ordId)
        if clOrdId is not None:
            params['clOrdId'] = str(clOrdId)

        data = self._request_with_params(POST, CANCEL_ORDER, params)["data"]
        return data

    def cancel_batch_orders(self, orders: Union[CancelOrder, Iterable[CancelOrder]]):
        orders_list = []
        if isinstance(orders, Order):
            orders_list.append(orders)
        else:
            orders_list = orders
        params = []

        for order in orders_list:
            param = dict()
            if order.instId is not None:
                params['instId'] = str(order.instId)
            if order.ordId is not None:
                params['ordId'] = str(order.ordId)
            if order.clOrdId is not None:
                params['clOrdId'] = str(order.clOrdId)
            params.append(param)

        data = self._request_with_params(POST, CANCEL_BATCH_ORDERS, params)["data"]
        return data

    def get_order(self, instId: str, ordId: Optional[str] = None, clOrdId: Optional[str] = None) -> Dict:
        params = {}
        if instId is not None:
            params['instId'] = str(instId)
        if ordId is not None:
            params['ordId'] = str(ordId)
        if clOrdId is not None:
            params['clOrdId'] = str(clOrdId)

        data = self._request_with_params(GET, ORDER, params)["data"]

        return data
