
from typing import Any, Dict, Union, Optional, Iterable
from enum import Enum

from typeguard import typechecked

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .objects.ccytype import CcyType
from .objects.posside import PosSide
from .objects.tdmode import TdMode
from .objects.ordertype import OrderType
from .objects.trgccy import TrgCCY
from .objects.triggerpxtype import TriggerPxType
from .objects.mgnmode import MgnModeT

@typechecked
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


@typechecked
class AmendOrder(object):
    def __init__(self,
            instId: str,
            cxlOnFail: Optional[bool] = False,
            ordId: Optional[str] = None,
            clOrdId: Optional[str] = None,
            reqId: Optional[str] = None,
            newSz: Optional[Union[float, int, str]] = None,
            newPx: Optional[Union[float, int, str]] = None,
            newTpTriggerPx: Optional[Union[float, int, str]] = None,
            newTpOrdPx: Optional[Union[float, int, str]] = None,
            newSlTriggerPx: Optional[Union[float, int, str]] = None,
            newSlOrdPx: Optional[Union[float, int, str]] = None,
            newTpTriggerPxType: Optional[Union[str, TriggerPxType]] = None,
            newSlTriggerPxType: Optional[Union[str, TriggerPxType]] = None,
        ) -> None:
        super().__init__()
        self.instId = instId
        self.cxlOnFail = cxlOnFail
        self.ordId = ordId
        self.clOrdId = clOrdId
        self.reqId = reqId
        self.newSz = newSz
        self.newPx = newPx
        self.newTpTriggerPx = newTpTriggerPx
        self.newTpOrdPx = newTpOrdPx
        self.newSlTriggerPx = newSlTriggerPx
        self.newSlOrdPx = newSlOrdPx
        self.newTpTriggerPxType = newTpTriggerPxType
        self.newSlTriggerPxType = newSlTriggerPxType

class CancelOrder(object):
    def __init__(self, instId: str, ordId: Optional[str] = None, clOrdId: Optional[str] = None) -> None:
        super().__init__()
        self.instId = instId
        self.ordId = ordId
        self.clOrdId = clOrdId

class TradeAPI(Client):

    def __init__(self, api_key: str, api_secret_key: str, passphrase: str, use_server_time: bool = False, test: bool = False, first: bool = False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

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
            if isinstance(sz, str):
                params['sz'] = sz
            else:
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
                if isinstance(order.sz, str):
                    params['sz'] = order.sz
                else:
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

    def amend_order(self, instId: str,
                    cxlOnFail: Optional[bool] = False,
                    ordId: Optional[str] = None,
                    clOrdId: Optional[str] = None,
                    reqId: Optional[str] = None,
                    newSz: Optional[Union[float, int, str]] = None,
                    newPx: Optional[Union[float, int, str]] = None,
                    newTpTriggerPx: Optional[Union[float, int, str]] = None,
                    newTpOrdPx: Optional[Union[float, int, str]] = None,
                    newSlTriggerPx: Optional[Union[float, int, str]] = None,
                    newSlOrdPx: Optional[Union[float, int, str]] = None,
                    newTpTriggerPxType: Optional[Union[str, TriggerPxType]] = None,
                    newSlTriggerPxType: Optional[Union[str, TriggerPxType]] = None,
                ) -> Dict[str, Any]:
        if ordId is None and clOrdId is None:
            raise ValueError("Order ID, one of ordId and clOrdId must have a value.")
        params = {}
        if instId is not None:
            params['instId'] = str(instId)
        if cxlOnFail is not None:
            params['cxlOnFail'] = cxlOnFail
        if ordId is not None:
            params['ordId'] = str(ordId)
        if clOrdId is not None:
            params['clOrdId'] = str(clOrdId)
        if reqId is not None:
            params['reqId'] = str(reqId)
        if newSz is not None:
            params['newSz'] = str(newSz)
        if newPx is not None:
            params['newPx'] = str(newPx)
        if newTpTriggerPx is not None:
            params['newTpTriggerPx'] = str(newTpTriggerPx)
        if newTpOrdPx is not None:
            params['newTpOrdPx'] = str(newTpOrdPx)
        if newSlTriggerPx is not None:
            params['newSlTriggerPx'] = str(newSlTriggerPx)
        if newSlOrdPx is not None:
            params['newSlOrdPx'] = str(newSlOrdPx)
        if newTpTriggerPxType is not None:
            params['newTpTriggerPxType'] = enum_to_str(newTpTriggerPxType)
        if newSlTriggerPxType is not None:
            params['newSlTriggerPxType'] = enum_to_str(newSlTriggerPxType)

        data = self._request_with_params(POST, AMEND_ORDER, params)["data"]

        return data

    def amend_batch_orders(self, orders: Union[AmendOrder, Iterable[AmendOrder]]) -> Dict[str, Any]:
        orders_list = []
        if isinstance(orders, AmendOrder):
            orders_list.append(orders)
        else:
            orders_list = orders
        params_total = []

        for order in orders_list:
            params = dict()
            if order.ordId is None and order.clOrdId is None:
                raise ValueError("Order ID, one of ordId and clOrdId must have a value.")
            if order.instId is not None:
                params['instId'] = str(order.instId)
            if order.cxlOnFail is not None:
                params['cxlOnFail'] = order.cxlOnFail
            if order.ordId is not None:
                params['ordId'] = str(order.ordId)
            if order.clOrdId is not None:
                params['clOrdId'] = str(order.clOrdId)
            if order.reqId is not None:
                params['reqId'] = str(order.reqId)
            if order.newSz is not None:
                params['newSz'] = str(order.newSz)
            if order.newPx is not None:
                params['newPx'] = str(order.newPx)
            if order.newTpTriggerPx is not None:
                params['newTpTriggerPx'] = str(order.newTpTriggerPx)
            if order.newTpOrdPx is not None:
                params['newTpOrdPx'] = str(order.newTpOrdPx)
            if order.newSlTriggerPx is not None:
                params['newSlTriggerPx'] = str(order.newSlTriggerPx)
            if order.newSlOrdPx is not None:
                params['newSlOrdPx'] = str(order.newSlOrdPx)
            if order.newTpTriggerPxType is not None:
                params['newTpTriggerPxType'] = enum_to_str(order.newTpTriggerPxType)
            if order.newSlTriggerPxType is not None:
                params['newSlTriggerPxType'] = enum_to_str(order.newSlTriggerPxType)
            params_total.append(params)

        data = self._request_with_params(POST, AMEND_BATCH_ORDERS, params_total)["data"]

        return data

    def close_position(self, instId: str,
                    mgnMode: MgnModeT,
                    posSide: Optional[Union[PosSide, str]] = None,
                    ccy: Optional[str] = None,
                    autoCxl: Optional[bool] = False,
                    clOrdId: Optional[str] = None,
                    tag: Optional[str] = None
                    ) -> Dict[str, Any]:
        params = {}
        if instId is not None:
            params['instId'] = str(instId)
        if posSide is not None:
            params['posSide'] = enum_to_str(posSide)
        if mgnMode is not None:
            params['mgnMode'] = enum_to_str(mgnMode)
        if ccy is not None:
            params['ccy'] = str(ccy)
        if autoCxl is not None:
            params['autoCxl'] = autoCxl
        if clOrdId is not None:
            params['clOrdId'] = str(clOrdId)
        if tag is not None:
            params['tag'] = str(tag)

        data = self._request_with_params(POST, CLOSE_POSITION, params)["data"]

        return data