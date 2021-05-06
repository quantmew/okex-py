
import hmac
import base64
from hashlib import sha256
import requests
import datetime
import json
import pandas as pd
from .exceptions import InvalidDataError, ParamsError


class OkAPI(object):
    domain = "https://www.okex.com"

    def __init__(self, key, secret_key, passphrase):
        self.key = key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def get_sign(self, timestamp, method, requestPath, body=''):
        content = timestamp + method + requestPath + body
        b64 = base64.b64encode(hmac.new(self.secret_key.encode(
        ), content.encode(), digestmod=sha256).digest()).decode()
        return b64

    def get_timestamp(self):
        utcnow = datetime.datetime.utcnow()
        return utcnow.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    def get_header(self, method, url, body=""):
        timestamp = self.get_timestamp()
        return {
            'OK-ACCESS-KEY': self.key,
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-SIGN': self.get_sign(timestamp, method, url, body),
            'OK-ACCESS-PASSPHRASE': self.passphrase
        }

    def get(self, category, method, params=None):
        url = "/api/v5/" + category + "/" + method
        if params is None:
            out = requests.get(self.domain + url,
                               headers=self.get_header("GET", url))
        else:
            out = requests.get(self.domain + url, params=params,
                               headers=self.get_header("GET", url))
        return out.text

    def post(self, category, method, params=None):
        body = json.dumps(params)
        url = "/api/v5/" + category + "/" + method
        headers = self.get_header("POST", url, body)
        headers['Content-Type'] = 'application/json'
        if params is None:
            out = requests.post(self.domain + url, headers=headers)
        else:
            out = requests.post(self.domain + url, data=body, headers=headers)
        return out.text

    def account_position_risk(self):
        out = self.get('account', 'account-position-risk')
        obj = json.loads(out)
        if obj['code'] == '0':
            return obj['data']
        else:
            raise Exception("")

    def market_ticker(self, instId):
        out = self.get('market', 'ticker', {'instId': instId})
        obj = json.loads(out)
        if obj['code'] == '0':
            return obj['data']
        else:
            raise Exception("")

    def history_candles(self, instId):
        out = self.get(
            'market',
            'history-candles',
            {
                'instId': instId
            }
        )
        obj = json.loads(out)
        if obj['code'] == '0':
            df = pd.DataFrame(obj['data'], columns=["ts", "o", "h", "l", "c", "vol", "volCcy"])
            df['ts'] = df['ts'].apply(lambda x: datetime.datetime.fromtimestamp(int(x)/1000))
            return df
        else:
            raise InvalidDataError(obj['code'] + ": " + obj['msg'])

    def order(self, instId, tdMode, side, ordType, sz):
        out = self.post(
            'trade',
            'order',
            {
                'instId': instId,
                'tdMode': tdMode,
                'side': side,
                'ordType': ordType,
                'sz': str(sz)
            }
        )
        obj = json.loads(out)
        print(obj)
        if obj['code'] == '0':
            return obj['data']
        else:
            raise InvalidDataError(obj['code'] + ": " + obj['msg'])
