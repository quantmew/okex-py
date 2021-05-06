
import hmac
import base64
from hashlib import sha256
import requests
import datetime

class OkAPI(object):
    domain = "https://www.okex.com"
    def __init__(self, key, secret_key, passphrase):
        self.key = key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def get_sign(self, timestamp, method, requestPath, body=''):
        content = timestamp + method + requestPath + body
        print(content)
        b64 = base64.b64encode(hmac.new(self.secret_key.encode(), content.encode(), digestmod=sha256).digest()).decode()
        print(b64)
        return b64

    def get_timestamp(self):
        utcnow = datetime.datetime.utcnow()
        return utcnow.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

    def account_position_risk(self):
        timestamp = self.get_timestamp()
        print(timestamp)
        url = "/api/v5/account/account-position-risk"
        
        out = requests.get(self.domain + url, headers={
            'OK-ACCESS-KEY': self.key,
            'OK-ACCESS-TIMESTAMP': timestamp,
            'OK-ACCESS-SIGN': self.get_sign(timestamp, 'GET', url),
            'OK-ACCESS-PASSPHRASE': self.passphrase
        })
        print(out.text)