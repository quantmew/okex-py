import datetime
from typing import Union, Optional, Iterable

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .insttype import InstType
from .ccytype import CcyType

import pandas as pd

class SystemAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, test=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def status(self, state:Optional[str]=None):
        params = {}
        if state is not None:
            params['state'] = state

        data = self._request_with_params(GET, INSTRUMENTS, params)["data"]

        return data
