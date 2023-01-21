
from typing import Any, Dict, Union, Optional, Iterable
from typeguard import check_argument_types, check_return_type

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .insttype import InstType
from .ccytype import CcyType
from .mgnmode import MgnMode
from .cttype import CtType
from .billtype import BillType, BillSubType
from okex.v5.trade_api import PosSide

import pandas as pd

from enum import Enum

class PosMode(Enum):
    LONG_SHORT_MODE = "long_short_mode"
    NET_MODE = "net_mode"

class AccountAPI(Client):
    def __init__(self, api_key: str, api_secret_key: str, passphrase: str, use_server_time: bool = False, test: bool = False, first: bool = False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def position_risk(self, instType: Optional[Union[InstType, str]] = None) -> Dict[str, Any]:
        """Get account position risk

        Args:
            instType (Optional[Union[InstType, str]], optional): instrument type. Defaults to None.

        Returns:
            Dict[str, Any]: position risk data
        """
        assert check_argument_types()
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        data = self._request_with_params(GET, POSITION_RISK, params)["data"]

        # df = pd.DataFrame(data)
        return data

    def balance(self, ccyType: Optional[Union[CcyType, str]] = None) -> Dict[str, Any]:
        """Get balance

        Args:
            ccyType (Optional[Union[CcyType, str]], optional): Single currency or multiple currencies (no more than 20) separated with comma, e.g. BTC or BTC,ETH. Defaults to None.

        Returns:
            Dict[str, Any]: balance data
        """
        assert check_argument_types()
        params = {}
        if ccyType is not None:
            params['ccyType'] = enum_to_str(ccyType)
        return self._request_with_params(GET, BALANCE, params)['data']

    # get specific currency info
    def positions(self, instType: Optional[Union[InstType, str]] = None, instId: Optional[str] = None, posId: Optional[Union[str, Iterable]] = None) -> Dict[str, Any]:
        assert check_argument_types()
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

    def bills(self, instType: Optional[Union[InstType, str]] = None,
                        ccyType: Optional[Union[InstType, str]] = None,
                        mgnMode: Optional[Union[MgnMode, str]] = None,
                        ctType: Optional[Union[CtType, str]] = None,
                        billType: Optional[Union[BillType, str]] = None,
                        billSubType: Optional[Union[BillSubType, str]] = None,
                        after: Optional[int] = None,
                        before: Optional[int] = None,
                        limit: Optional[int] = None
                        ) -> pd.DataFrame:
        assert check_argument_types()
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if ccyType is not None:
            params['ccyType'] = enum_to_str(ccyType)
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

    def bills_archive(self, instType: Optional[Union[InstType, str]] = None,
                        ccyType: Optional[Union[InstType, str]] = None,
                        mgnMode: Optional[Union[MgnMode, str]] = None,
                        ctType: Optional[Union[CtType, str]] = None,
                        billType: Optional[Union[BillType, str]] = None,
                        billSubType: Optional[Union[BillSubType, str]] = None,
                        after: Optional[int] = None,
                        before: Optional[int] = None,
                        limit: Optional[int] = None
                        ) -> pd.DataFrame:
        assert check_argument_types()
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if ccyType is not None:
            params['ccyType'] = enum_to_str(ccyType)
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
        assert check_argument_types()
        params = {}
        params['posMode'] = enum_to_str(posMode)
        data = self._request_without_params(POST, SET_POSITION_MODE, params)['data']
        return data
    
    def set_leverage(self, lever: Union[int, str],
                    mgnMode: Union[MgnMode, str],
                    instId: Optional[str] = None,
                    ccyType: Optional[Union[CcyType, str]] = None,
                    posSide: Optional[Union[PosSide, str]] = None) -> Dict[str, Any]:
        assert check_argument_types()
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