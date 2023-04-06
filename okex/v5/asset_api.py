import datetime
from typing import Union, Optional, Iterable

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .objects.insttype import InstType
from .objects.ccytype import CcyType, CcyTypeT

import pandas as pd
from typeguard import typechecked

@typechecked
class AssetAPI(Client):

    def __init__(self, api_key: str, api_secret_key: str, passphrase: str, use_server_time: bool = False, test: bool = False, first: bool = False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def currencies(self):
        data = self._request_without_params(GET, CURRENCIES)["data"]

        return data

    def balances(self, ccy: CcyTypeT):
        params = {}
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)

        data = self._request_with_params(GET, BALANCES, params)["data"]

        return data

    def deposit_address(self, ccy: CcyTypeT):
        params = {}
        if ccy is not None:
            params['ccy'] = enum_to_str(ccy)

        data = self._request_with_params(GET, DEPOSIT_ADDRESS, params)["data"]

        return data

    def balances(self, ccy: Optional[Union[CcyType, str, Iterable[CcyTypeT]]] = None):
        params = {}
        if ccy is not None:
            if isinstance(ccy, Iterable):
                ccyList = list(ccy)
                if len(ccyList) > 20:
                    raise OkexParamsException("支持多个ccy查询（不超过20个）")
                else:
                    params['ccy'] = iterable_to_str(ccyList)
            else:
                params['ccy'] = enum_to_str(ccy)

        data = self._request_with_params(GET, BALANCES, params)["data"]

        return data