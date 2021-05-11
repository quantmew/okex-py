
from typing import Union, Optional, Iterable

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .insttype import InstType
from .ccytype import CcyType
from .mgnmode import MgnMode
from .cttype import CtType
from .billtype import BillType, BillSubType

import pandas as pd
class AccountAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    # get account position risk
    def position_risk(self, instType: Optional[Union[InstType, str]] = None):
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        data = self._request_with_params(GET, POSITION_RISK, params)["data"]

        # df = pd.DataFrame(data)
        return data

    # get balance
    def balance(self, ccyType: Optional[Union[CcyType, str]] = None):
        params = {}
        if ccyType is not None:
            params['ccyType'] = enum_to_str(ccyType)
        return self._request_with_params(GET, BALANCE, params)['data']

    # get specific currency info
    def positions(self, instType: Optional[Union[InstType, str]] = None, instId: Optional[str] = None, posId: Optional[Union[str, Iterable]] = None):
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
                        ):
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
                        ):
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

    def config(self):
        data = self._request_without_params(GET, CONFIG)['data']
        return data
