
'''
Here is the okex api example.

'''

import okex.v5.account_api as account
import okex.v5.market_api as market
import okex.v5.public_api as public
import okex.v5.trade_api as trade
import json
import datetime

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

time = get_timestamp()


if __name__ == '__main__':

    with open('api.json', 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
    api_key = obj['api_key']
    secret_key = obj['secret_key']
    passphrase = obj['passphrase']

    # param use_server_time's value is False if is True will use server timestamp
    # param test's value is False if is True will use simulative trading
    test = True
    # account api test
    # 资金账户API
    accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False, test=test)
    # 查看账户持仓风险
    from okex.v5.insttype import InstType
    result = accountAPI.position_risk(instType=InstType.MARGIN)
    # print(result)

    # 查看账户余额
    from okex.v5.ccytype import CcyType
    result = accountAPI.balance(ccyType=CcyType.BTC)
    # print(result)

    # 查看持仓信息
    from okex.v5.insttype import InstType
    result = accountAPI.positions()
    # print(result)

    # 账单流水查询（近七天）
    result = accountAPI.bills()
    # print(result)

    # 账单流水查询（近三个月）
    result = accountAPI.bills_archive()
    # print(result)

    # market
    marketAPI = market.MarketAPI(api_key, secret_key, passphrase, False, test=test)
    # 获取所有产品行情信息
    result = marketAPI.tickers(InstType.SWAP)
    # print(result)
    # 获取单个产品行情信息
    result = marketAPI.ticker('BTC-USD-SWAP')
    # print(result)
    # 获取指数行情
    result = marketAPI.tickers(InstType.SWAP)
    # print(result)
    # 获取产品深度
    result = marketAPI.books('BTC-USD-SWAP')
    # print(result)
    # 获取所有交易产品K线数据
    result = marketAPI.candles(instId='BTC-USD-SWAP')
    print(result)
    # 获取交易产品历史K线数据
    result = marketAPI.history_candles(instId='BTC-USD-SWAP')
    # print(result)

    # public
    publicAPI = public.PublicAPI(api_key, secret_key, passphrase, False, test=test)
    result = publicAPI.instruments(InstType.SWAP)
    print(result)

    # trade
    from okex.v5.trade_api import TdMode, OrderType
    tradeAPI = trade.TradeAPI(api_key, secret_key, passphrase, False, test=test)
    # 卖出SHIB试试
    # result = tradeAPI.order('SHIB-USDT', TdMode.CASH, OrderType.MARKET, -1000000)
    # print(result)
    # 打印订单信息
    # result = tradeAPI.get_order(instId='SHIB-USDT')
    # print(result)