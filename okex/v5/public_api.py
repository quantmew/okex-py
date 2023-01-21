import datetime
from typing import Any, Dict, Union, Optional, Iterable
from typeguard import check_argument_types, check_return_type

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .objects.insttype import InstType
from .objects.ccytype import CcyType

import pandas as pd

class PublicAPI(Client):

    def __init__(self, api_key: str, api_secret_key: str, passphrase: str, use_server_time: bool = False, test: bool = False, first: bool = False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def instruments(self, instType: Union[InstType, str], uly: Optional[str]=None, instId: Optional[str]=None):
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if uly is not None:
            params['uly'] = uly
        if instId is not None:
            params['instId'] = instId
        data = self._request_with_params(GET, INSTRUMENTS, params)["data"]

        df = pd.DataFrame(data)
        df = df.apply(pd.to_numeric, errors='ignore')
        return df

    def delivery_exercise_history(self, instType: Union[InstType, str],
            uly: str,
            after: Optional[Union[int, str]]=None,
            before: Optional[Union[int, str]]=None, 
            limit: Optional[Union[int, str]]=None):
        pass

    def open_interest(self,
            instType: Union[InstType, str],
            uly: Optional[str]=None,
            instId: Optional[str]=None) -> Dict[str, Any]:
        params = {}
        params['instType'] = str(instType)
        if uly is not None:
            params['uly'] = str(uly)
        if instId is not None:
            params['instId'] = str(instId)

        data = self._request_with_params(GET, OPEN_INTEREST, params)["data"]
        return data

    def funding_rate(self, instId: str):
        params = {}
        params['instId'] = str(instId)
        data = self._request_with_params(GET, FUNDING_RATE, params)["data"]
        return data

    def funding_rate_history(self, instId: str,
                    before: Optional[Union[int, str]]=None,
                    after: Optional[Union[int, str]]=None,
                    limit: Optional[Union[int, str]]=None) -> pd.DataFrame:
        params = {}
        params['instId'] = str(instId)
        if before is not None:
            params['before'] = str(before)
        if after is not None:
            params['after'] = str(after)
        if limit is not None:
            params['limit'] = str(limit)
        data = self._request_with_params(GET, FUNDING_RATE_HISTORY, params)["data"]
        return data

    def price_limit(self, instId: str) -> Dict[str, Any]:
        params = {}
        params['instId'] = str(instId)
        data = self._request_with_params(GET, PRICE_LIMIT, params)["data"]
        return data

    def time(self) -> Dict[str, Any]:
        data = self._request_without_params(GET, TIME)["data"]
        return data