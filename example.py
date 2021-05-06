
import json
from okex.client import OkAPI


with open('api.json', 'r', encoding='utf-8') as f:
    obj = json.loads(f.read())
key = obj['key']
secret_key = obj['secret_key']
passphrase = obj['passphrase']
api = OkAPI(key, secret_key, passphrase)

api.account_position_risk()
out = api.market_ticker('ETC-USDT')
print(out)
out = api.history_candles('ETC-USDT')
print(out)