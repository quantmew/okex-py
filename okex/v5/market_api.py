
from typing import Union, Optional, Iterable

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .insttype import InstType

import pandas as pd

class MarketAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def tickers(self, instType: InstType, uly:str=None):
        params = {}
        if instType is not None:
            params['instType'] = enum_to_str(instType)
        if uly is not None:
            params['uly'] = uly
        data = self._request_with_params(GET, TICKERS, params)["data"]

        df = pd.DataFrame(data)
        return df

    def ticker(self, instId: str):
        params = {}
        if instId is not None:
            params['instId'] = instId
        data = self._request_with_params(GET, TICKERS, params)["data"]

        df = pd.DataFrame(data)
        return df

    def index_tickers(self):
        pass

    def books(self):
        pass

    def candles(self):
        pass

    def history_candles(self):
        pass