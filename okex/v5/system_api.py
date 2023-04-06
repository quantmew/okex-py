import datetime
from typing import Dict, List, Union, Optional, Iterable

from .client import Client
from .consts import *
from .utils import enum_to_str, iterable_to_str
from ..exceptions import OkexParamsException

from .objects.insttype import InstType
from .objects.ccytype import CcyType

import pandas as pd
from typeguard import typechecked

@typechecked
class SystemAPI(Client):

    def __init__(self, api_key: str, api_secret_key: str, passphrase: str, use_server_time: bool = False, test: bool = False, first: bool = False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, test, first)

    def status(self, state:Optional[str] = None) -> List[Dict[str, str]]:
        params = {}
        if state is not None:
            params['state'] = state

        data = self._request_with_params(GET, STATUS, params)["data"]

        return data
