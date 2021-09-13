API_URL = 'https://www.okex.com'

CONTENT_TYPE = 'Content-Type'
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'

ACEEPT = 'Accept'
COOKIE = 'Cookie'
LOCALE = 'Locale='

APPLICATION_JSON = 'application/json'

GET = "GET"
POST = "POST"
DELETE = "DELETE"

SERVER_TIMESTAMP_URL = '/api/general/v5/time'

# account
POSITION_RISK = '/api/v5/account/account-position-risk'
BALANCE = '/api/v5/account/balance'
POSITIONS = '/api/v5/account/positions'
BILLS = '/api/v5/account/bills'
BILLS_ARCHIVE = '/api/v5/account/bills-archive'
CONFIG = '/api/v5/account/config'


# asset
DEPOSIT_ADDRESS = '/api/v5/asset/deposit-address'
BALANCES = '/api/v5/asset/balances'


# market
TICKERS = '/api/v5/market/tickers'
TICKER = '/api/v5/market/ticker'
INDEX_TICKERS = '/api/v5/market/index-tickers'
BOOKS = '/api/v5/market/books'
CANDLES = '/api/v5/market/candles'
HISTORY_CANDLES = '/api/v5/market/history-candles'

# public
INSTRUMENTS = '/api/v5/public/instruments'


# trade
ORDER = '/api/v5/trade/order'
BATCH_ORDERS = '/api/v5/trade/batch-orders'
CANCEL_ORDER = '/api/v5/trade/cancel-order'
CANCEL_BATCH_ORDERS = '/api/v5/trade/cancel-batch-orders'