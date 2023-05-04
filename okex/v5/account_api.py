
from typing import Any, Dict, Literal, Union, Optional, Iterable
from typeguard import typechecked

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .objects.insttype import InstType, InstTypeT
from .objects.ccytype import CcyType, CcyTypeT
from .objects.tdmode import TdMode
from .objects.mgnmode import MgnMode, MgnModeT
from .objects.cttype import CtType
from .objects.billtype import BillType, BillSubType
from .objects.posside import PosSide

import pandas as pd

from enum import Enum


class PosMode(Enum):
    LONG_SHORT_MODE = "long_short_mode"
    NET_MODE = "net_mode"

@typechecked
class AccountAPI(Client):
    def __init__(self, api_key: str, api_secret_key: str, passphrase: str, use_server_time: bool = False, test: bool = False, first: bool = False):
        Client.__init__(self, api_key, api_secret_key,
                        passphrase, use_server_time, test, first)

    def position_risk(self, instType: Optional[InstTypeT] = None) -> Dict[str, Any]:
        """Get account position risk

        Args:
            instType (Optional[InstTypeT], optional): instrument type. Defaults to None.

        Returns:
            Dict[str, Any]: position risk data
        """
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        data = self._request_with_params(GET, POSITION_RISK, params)["data"]

        # df = pd.DataFrame(data)
        return data

    def balance(self, ccy: Optional[Union[CcyType, str]] = None) -> Dict[str, Any]:
        """Get balance

        Args:
            ccy (Optional[Union[CcyType, str]], optional): Single currency or multiple currencies (no more than 20) separated with comma, e.g. BTC or BTC,ETH. Defaults to None.

        Returns:
            Dict[str, Any]: balance data
        """
        params = {}
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)
        return self._request_with_params(GET, BALANCE, params)['data']

    # get specific currency info
    def positions(self, instType: Optional[InstTypeT] = None,
                  instId: Optional[str] = None,
                  posId: Optional[Union[str, Iterable]] = None
                ) -> Dict[str, Any]:
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if instId is not None:
            params['instId'] = instId
        if posId is not None:
            posIdList = list(posId)
            if len(posIdList) > 20:
                raise OkexParamsException("支持多个posId查询（不超过20个）")
            else:
                params['instId'] = iterable_to_str(posIdList)

        data = self._request_with_params(GET, POSITIONS, params)['data']
        return data
    
    def positions_history(self, instType='', instId='', mgnMode='', type='', posId='', after='', before='', limit=''):
        params = {
            'instType': instType,
            'instId': instId,
            'mgnMode': mgnMode,
            'type': type,
            'posId': posId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return self._request_with_params(GET, POSITIONS_HISTORY, params)

    def bills(self, instType: Optional[InstTypeT] = None,
              ccy: Optional[CcyTypeT] = None,
              mgnMode: Optional[MgnModeT] = None,
              ctType: Optional[Union[CtType, str]] = None,
              billType: Optional[Union[BillType, str]] = None,
              billSubType: Optional[Union[BillSubType, str]] = None,
              after: Optional[int] = None,
              before: Optional[int] = None,
              limit: Optional[int] = None
              ) -> pd.DataFrame:
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)
        if mgnMode is not None:
            params['mgnMode'] = enum_to_str(mgnMode)
        if ctType is not None:
            params['ctType'] = enum_to_str(ctType)
        if billType is not None:
            params['type'] = enum_to_str(billType)
        if billSubType is not None:
            params['subType'] = enum_to_str(billSubType)
        if after is not None:
            params['after'] = str(after)
        if before is not None:
            params['before'] = str(before)
        if limit is not None:
            params['befolimitre'] = str(limit)

        data = self._request_with_params(GET, BILLS, params)['data']

        df = pd.DataFrame(data, columns=["instType", "billId", "type", "subType", "ts", "balChg", "posBalChg",
                                         "bal", "posBal", "sz", "ccy", "pnl", "fee", "mgnMode",
                                         "instId", "ordId", "from", "to", "notes"])

        return df

    def bills_archive(self, instType: Optional[InstTypeT] = None,
                      ccy: Optional[CcyTypeT] = None,
                      mgnMode: Optional[MgnModeT] = None,
                      ctType: Optional[Union[CtType, str]] = None,
                      billType: Optional[Union[BillType, str]] = None,
                      billSubType: Optional[Union[BillSubType, str]] = None,
                      after: Optional[int] = None,
                      before: Optional[int] = None,
                      limit: Optional[int] = None
                      ) -> pd.DataFrame:
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)
        if mgnMode is not None:
            params['mgnMode'] = enum_to_str(mgnMode)
        if ctType is not None:
            params['ctType'] = enum_to_str(ctType)
        if billType is not None:
            params['type'] = enum_to_str(billType)
        if billSubType is not None:
            params['subType'] = enum_to_str(billSubType)
        if after is not None:
            params['after'] = str(after)
        if before is not None:
            params['before'] = str(before)
        if limit is not None:
            params['befolimitre'] = str(limit)

        data = self._request_with_params(GET, BILLS_ARCHIVE, params)['data']

        df = pd.DataFrame(data, columns=["instType", "billId", "type", "subType", "ts", "balChg", "posBalChg",
                                         "bal", "posBal", "sz", "ccy", "pnl", "fee", "mgnMode",
                                         "instId", "ordId", "from", "to", "notes"])

        return df

    def config(self) -> Dict[str, Any]:
        data = self._request_without_params(GET, CONFIG)['data']
        return data

    def set_position_mode(self, posMode: Union[str, PosMode]) -> Dict[str, Any]:
        params = {}
        params['posMode'] = enum_to_str(posMode)
        data = self._request_without_params(
            POST, SET_POSITION_MODE, params)['data']
        return data

    def set_leverage(self, lever: Union[int, str],
                     mgnMode: MgnModeT,
                     instId: Optional[str] = None,
                     ccyType: Optional[CcyTypeT] = None,
                     posSide: Optional[Union[PosSide, str]] = None) -> Dict[str, Any]:
        params = {}
        params["lever"] = str(lever)
        params["mgnMode"] = enum_to_str(mgnMode)
        if instId is not None:
            params['instId'] = str(instId)
        if ccyType is not None:
            params['ccyType'] = enum_to_str(ccyType)
        if posSide is not None:
            params['posSide'] = enum_to_str(posSide)

        data = self._request_with_params(POST, SET_LEVERAGE, params)['data']
        return data

    def max_size(self, instId: str,
                 tdMode: Union[TdMode, str],
                 ccy: Optional[Union[CcyType, str]] = None,
                 px: Optional[Union[float, int, str]] = None
                 ) -> Dict[str, Any]:
        params = {}
        params["instId"] = str(instId)
        params["tdMode"] = enum_to_str(tdMode)
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)
        if px is not None:
            params['px'] = str(px)
        return self._request_with_params(GET, MAX_SIZE, params)

    def max_avail_size(self, instId: str,
                       tdMode: Union[TdMode, str],
                       ccy: Optional[Union[InstType, str]] = None,
                       px: Optional[Union[float, int, str]] = None
                       ) -> Dict[str, Any]:
        params = {}
        params["instId"] = str(instId)
        params["tdMode"] = enum_to_str(tdMode)
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)
        if px is not None:
            params['px'] = str(px)
        return self._request_with_params(GET, MAX_SIZE, params)

    def margin_balance(self, instId: str,
                          posSide: Union[PosSide, str],
                          type: Literal["add", "reduce"],
                          amt: Union[float, int, str],
                          ccy: Optional[CcyTypeT] = None,
                          loanTrans: Optional[bool]=None):
        params = {}
        params["instId"] = str(instId)
        params["posSide"] = enum_to_str(posSide)
        params["type"] = str(type)
        params["amt"] = str(amt)
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)
        if loanTrans is not None:
            params['loanTrans'] = str(loanTrans)
        else:
            params['loanTrans'] = False
        return self._request_with_params(POST, MARGIN_BALANCE, params)

    def leverage_info(self, instId: str, mgnMode: MgnModeT):
        params = {'instId': instId, 'mgnMode': enum_to_str(mgnMode)}
        return self._request_with_params(GET, LEVERAGE_INFO, params)

    def max_loan(self, instId: str, mgnMode: MgnModeT, mgnCcy: Optional[CcyTypeT]=None):
        params = {}
        params["instId"] = str(instId)
        params["mgnMode"] = enum_to_str(mgnMode)
        if mgnCcy is not None:
            params["mgnCcy"] = enum_to_str(mgnCcy)
        return self._request_with_params(GET, MAX_LOAN, params)

    def trade_fee(self, instType: InstTypeT,
                  instId: Optional[str] = None,
                  uly: Optional[str] = None,
                  instFamily: Optional[str] = None):
        params = {}
        params["instType"] = enum_to_str(instType)
        if instId is not None:
            params["instId"] = str(instId)
        if uly is not None:
            params["uly"] = str(uly)
        if instFamily is not None:
            params["instFamily"] = str(instFamily)
        return self._request_with_params(GET, TRADE_FEE, params)

    def interest_accrued(self,
                         type: Optional[Union[str, int]]=2,
                         ccy: Optional[CcyTypeT] = None,
                         instId: Optional[str] = None,
                         mgnMode: Optional[MgnModeT]=None,
                         after: Optional[Union[str, int]]=None,
                         before: Optional[Union[str, int]]=None,
                         limit: Optional[Union[str, int]]=None
        ):

        params = {}
        if type is not None:
            params["type"] = str(type)
        if ccy is not None:
            params["ccy"] = enum_to_str(ccy)
        if instId is not None:
            params["instId"] = str(instId)
        if mgnMode is not None:
            params["mgnMode"] = enum_to_str(mgnMode)
        if after is not None:
            params["after"] = str(after)
        if before is not None:
            params["before"] = enum_to_str(before)
        if limit is not None:
            params["limit"] = str(limit)
        return self._request_with_params(GET, INTEREST_ACCRUED, params)

    def interest_rate(self, ccy: Optional[CcyTypeT] = None):
        params = {}
        if ccy is not None:
            params["ccy"] = str(ccy)
        return self._request_with_params(GET, INTEREST_RATE, params)

    def set_greeks(self, greeksType):
        params = {'greeksType': greeksType}
        return self._request_with_params(POST, SET_GREEKS, params)

    def set_isolated_mode(self, isoMode, type):
        params = {'isoMode': isoMode, 'type': type}
        return self._request_with_params(POST, ISOLATED_MODE, params)

    def max_withdrawal(self, ccy=''):
        params = {'ccy': ccy}
        return self._request_with_params(GET, MAX_WITHDRAWAL, params)

    def borrow_repay(self, ccy='', side='', amt=''):
        params = {'ccy': ccy, 'side': side, 'amt': amt}
        return self._request_with_params(POST, BORROW_REPAY, params)

    def get_borrow_repay_history(self, ccy='', after='', before='', limit=''):
        params = {'ccy': ccy, 'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, BORROW_REPAY_HISTORY, params)

    def interest_limits(self, type='', ccy=''):
        params = {'type': type, 'ccy': ccy}
        return self._request_with_params(GET, INTEREST_LIMITS, params)

    def simulated_margin(self, instType='', inclRealPos=True, instId='', pos=''):
        params = {'instType': instType, 'inclRealPos': inclRealPos,
                  'instId': instId, 'pos': pos, }
        return self._request_with_params(POST, SIMULATED_MARGIN, params)

    def greeks(self, ccy=''):
        params = {'ccy': ccy}
        return self._request_with_params(GET, GREEKS, params)

    def account_position_tiers(self, instType='', uly='', instFamily=''):
        params = {
            'instType': instType,
            'uly': uly,
            'instFamily': instFamily
        }
        return self._request_with_params(GET, ACCOUNT_POSITION_TIERS, params)
