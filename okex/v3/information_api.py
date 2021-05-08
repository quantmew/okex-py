from .client import Client
from .consts import *


class InformationAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time)

    def get_long_short_ratio(self, currency, start='', end='', granularity=''):
        params = {}
        if start:
            params['start'] = start
        if end:
            params['end'] = end
        if granularity:
            params['granularity'] = granularity

        return self._request_with_params(GET, INFORMATION + str(currency) + '/long_short_ratio', params)

    def get_volume(self, currency, start='', end='', granularity=''):
        params = {}
        if start:
            params['start'] = start
        if end:
            params['end'] = end
        if granularity:
            params['granularity'] = granularity

        return self._request_with_params(GET, INFORMATION + str(currency) + '/volume', params)

    def get_taker(self, currency, start='', end='', granularity=''):
        params = {}
        if start:
            params['start'] = start
        if end:
            params['end'] = end
        if granularity:
            params['granularity'] = granularity

        return self._request_with_params(GET, INFORMATION + str(currency) + '/taker', params)

    def get_sentiment(self, currency, start='', end='', granularity=''):
        params = {}
        if start:
            params['start'] = start
        if end:
            params['end'] = end
        if granularity:
            params['granularity'] = granularity

        return self._request_with_params(GET, INFORMATION + str(currency) + '/sentiment', params)

    def get_margin(self, currency, start='', end='', granularity=''):
        params = {}
        if start:
            params['start'] = start
        if end:
            params['end'] = end
        if granularity:
            params['granularity'] = granularity

        return self._request_with_params(GET, INFORMATION + str(currency) + '/margin', params)
