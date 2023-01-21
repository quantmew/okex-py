# API_URL = 'https://www.okex.com'
API_URL = 'https://www.okx.com'
WS_PUBLIC_URL = "wss://ws.okx.com:8443/ws/v5/public"
WS_PRIVATE_URL = "wss://ws.okx.com:8443/ws/v5/private"
WS_PUBLIC_TEST_URL = "wss://wspap.okx.com:8443/ws/v5/public?brokerId=9999"
WS_PRIVATE_TEST_URL = "wss://wspap.okx.com:8443/ws/v5/private?brokerId=9999"

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
SET_POSITION_MODE = '/api/v5/account/set-position-mode'
SET_LEVERAGE = "/api/v5/account/set-leverage"

# asset
CURRENCIES = '/api/v5/asset/currencies'
BALANCES = '/api/v5/asset/balances'
ASSET_VALUATION = '/api/v5/asset/asset-valuation'
TRANSFER = '/api/v5/asset/transfer'
TRANSFER_STATE = '/api/v5/asset/transfer-state'
BILLS = '/api/v5/asset/bills'
DEPPOSIT_LIGHTNING = '/api/v5/asset/deposit-lightning'
DEPOSIT_ADDRESS = '/api/v5/asset/deposit-address'
DEPOSIT_HISTORY = '/api/v5/asset/deposit-history'


# market
TICKERS = '/api/v5/market/tickers'
TICKER = '/api/v5/market/ticker'
INDEX_TICKERS = '/api/v5/market/index-tickers'
BOOKS = '/api/v5/market/books'
CANDLES = '/api/v5/market/candles'
HISTORY_CANDLES = '/api/v5/market/history-candles'
INDEX_CANDLES = '/api/v5/market/index-candles'
MARK_PRICE_CANDLES = '/api/v5/market/mark-price-candles'
TRADES = '/api/v5/market/trades'
PLATFORM_24_VOLUME = '/api/v5/market/platform-24-volume'
OPEN_ORACLE = '/api/v5/market/open-oracle'
EXCHANGE_RATE = '/api/v5/market/exchange-rate'
INDEX_COMPONENTS = '/api/v5/market/index-components'

# public
INSTRUMENTS = '/api/v5/public/instruments'
OPEN_INTEREST = '/api/v5/public/open-interest'
FUNDING_RATE = '/api/v5/public/funding-rate'
FUNDING_RATE_HISTORY = '/api/v5/public/funding-rate-history'
PRICE_LIMIT = '/api/v5/public/price-limit'
OPT_SUMMARY = '/api/v5/public/opt-summary'
ESTIMATED_PRICE = '/api/v5/public/estimated-price'
TIME = '/api/v5/public/time'
MARK_PRICE = '/api/v5/public/mark-price'

# trade
ORDER = '/api/v5/trade/order'
BATCH_ORDERS = '/api/v5/trade/batch-orders'
CANCEL_ORDER = '/api/v5/trade/cancel-order'
CANCEL_BATCH_ORDERS = '/api/v5/trade/cancel-batch-orders'

# system
STATUS = '/api/v5/system/status'