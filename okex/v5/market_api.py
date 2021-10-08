import datetime
from typing import Union, Optional, Iterable

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .insttype import InstType
from .ccytype import CcyType

import pandas as pd

class MarketAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def tickers(self, instType: InstType, uly: Optional[str]=None) -> pd.DataFrame:
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if uly is not None:
            params['uly'] = uly
        data = self._request_with_params(GET, TICKERS, params)["data"]

        df = pd.DataFrame(data)
        df = df.apply(pd.to_numeric, errors='ignore')
        df['ts'] = df['ts'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1000))
        return df

    def ticker(self, instId: str) -> pd.DataFrame:
        params = {}
        if instId is not None:
            params['instId'] = instId
        data = self._request_with_params(GET, TICKER, params)["data"]

        df = pd.DataFrame(data)
        df = df.apply(pd.to_numeric, errors='ignore')
        df['ts'] = df['ts'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1000))
        return df

    def index_tickers(self, quoteCcy: Optional[Union[CcyType, str]]=None, instId: Optional[str]=None) -> pd.DataFrame:
        params = {}
        if quoteCcy is not None:
            params['quoteCcy'] = enum_to_str(quoteCcy)
        if instId is not None:
            params['instId'] = instId
        data = self._request_with_params(GET, INDEX_TICKERS, params)["data"]

        df = pd.DataFrame(data)
        df = df.apply(pd.to_numeric, errors='ignore')
        return df

    def books(self, instId: str, sz: Optional[Union[int, str]]=None):
        params = {}
        if instId is not None:
            params['instId'] = instId
        if sz is not None:
            params['sz'] = str(sz)
        data = self._request_with_params(GET, BOOKS, params)["data"]

        return data

    def candles(self, instId: str,
                    after: Optional[Union[int, str]]=None,
                    before: Optional[Union[int, str]]=None,
                    bar: Optional[str]=None,
                    limit: Optional[Union[int, str]]=None) -> pd.DataFrame:
        params = {}
        if instId is not None:
            params['instId'] = str(instId)
        if after is not None:
            params['after'] = str(after)
        if before is not None:
            params['before'] = str(before)
        if bar is not None:
            params['bar'] = str(bar)
        if limit is not None:
            params['limit'] = str(limit)
        data = self._request_with_params(GET, CANDLES, params)["data"]

        df = pd.DataFrame(data, columns=["ts", "o", "h", "l", "c", "vol", "volCcy"])
        df = df.apply(pd.to_numeric, errors='ignore')
        df['ts'] = df['ts'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1000))
        return df


    def history_candles(self, instId: str,
                    after: Optional[Union[int, str]]=None,
                    before: Optional[Union[int, str]]=None,
                    bar: Optional[str]=None,
                    limit: Optional[Union[int, str]]=None) -> pd.DataFrame:
        params = {}
        if instId is not None:
            params['instId'] = str(instId)
        if after is not None:
            params['after'] = str(after)
        if before is not None:
            params['before'] = str(before)
        if bar is not None:
            params['bar'] = str(bar)
        if limit is not None:
            params['limit'] = str(limit)
        data = self._request_with_params(GET, CANDLES, params)["data"]

        df = pd.DataFrame(data, columns=["ts", "o", "h", "l", "c", "vol", "volCcy"])
        df = df.apply(pd.to_numeric, errors='ignore')
        df['ts'] = df['ts'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1000))
        return df