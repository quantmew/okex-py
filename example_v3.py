import okex.account_api as account
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import okex.swap_api as swap
import okex.index_api as index
import okex.option_api as option
import okex.system_api as system
import okex.information_api as information
import json
import datetime

def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"

time = get_timestamp()

if __name__ == '__main__':

    api_key = ""
    secret_key = ""
    passphrase = ""

    # param use_server_time's value is False if is True will use server timestamp
    # param test's value is False if is True will use simulative trading

# account api test
# 资金账户API
    accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
    # 资金账户信息
    # result = accountAPI.get_wallet()
    # 单一币种账户信息
    # result = accountAPI.get_currency('')
    # 资金划转
    # result = accountAPI.coin_transfer(currency='', amount='', account_from='', account_to='', type='', sub_account='', instrument_id='', to_instrument_id='')
    # 提币
    # result = accountAPI.coin_withdraw(currency='', amount='', destination='', to_address='', trade_pwd='', fee='')
    # 账单流水查询
    # result = accountAPI.get_ledger_record(currency='', after='', before='', limit='', type='')
    # 获取充值地址
    # result = accountAPI.get_top_up_address('')
    # 获取账户资产估值
    # result = accountAPI.get_asset_valuation(account_type='', valuation_currency='')
    # 获取子账户余额信息
    # result = accountAPI.get_sub_account('')
    # 查询所有币种的提币记录
    # result = accountAPI.get_coins_withdraw_record()
    # 查询单个币种提币记录
    # result = accountAPI.get_coin_withdraw_record('')
    # 获取所有币种充值记录
    # result = accountAPI.get_top_up_records()
    # 获取单个币种充值记录
    # result = accountAPI.get_top_up_record(currency='', after='', before='', limit='')
    # 获取币种列表
    # result = accountAPI.get_currencies()
    # 提币手续费
    # result = accountAPI.get_coin_fee('')

# spot api test
# 币币API
    spotAPI = spot.SpotAPI(api_key, secret_key, passphrase, False)
    # 币币账户信息
    # result = spotAPI.get_account_info()
    # 单一币种账户信息
    # result = spotAPI.get_coin_account_info('')
    # 账单流水查询
    # result = spotAPI.get_ledger_record(currency='', after='', before='', limit='', type='')
    # 下单
    # result = spotAPI.take_order(instrument_id='', side='', client_oid='', type='', size='', price='', order_type='0', notional='')
    # 批量下单
    # result = spotAPI.take_orders([
    #     {'instrument_id': '', 'side': '', 'type': '', 'price': '', 'size': ''},
    #     {'instrument_id': '', 'side': '', 'type': '', 'price': '', 'size': ''}
    # ])
    # 撤销指定订单
    # result = spotAPI.revoke_order(instrument_id='', order_id='', client_oid='')
    # 批量撤销订单
    # result = spotAPI.revoke_orders([
    #     {'instrument_id': '', 'order_ids': ['', '']},
    #     {'instrument_id': '', 'order_ids': ['', '']}
    # ])
    # 获取订单列表
    # result = spotAPI.get_orders_list(instrument_id='', state='', after='', before='', limit='')
    # 获取所有未成交订单
    # result = spotAPI.get_orders_pending(instrument_id='', after='', before='', limit='')
    # 获取订单信息
    # result = spotAPI.get_order_info(instrument_id='', order_id='', client_oid='')
    # 获取成交明细
    # result = spotAPI.get_fills(instrument_id='', order_id='', after='', before='', limit='')
    # 委托策略下单
    # result = spotAPI.take_order_algo(instrument_id='', mode='', order_type='', size='', side='', trigger_price='', algo_price='', algo_type='')
    # 委托策略撤单
    # result = spotAPI.cancel_algos(instrument_id='', algo_ids=['',''], order_type='')
    # 获取当前账户费率
    # result = spotAPI.get_trade_fee()
    # 获取委托单列表
    # result = spotAPI.get_order_algos(instrument_id='', order_type='', status='', algo_id='', before='', after='', limit='')
    # 公共-获取币对信息
    # result = spotAPI.get_coin_info()
    # 公共-获取深度数据
    # result = spotAPI.get_depth(instrument_id='', size='', depth='')
    # 公共-获取全部ticker信息
    # result = spotAPI.get_ticker()
    # 公共-获取某个ticker信息
    # result = spotAPI.get_specific_ticker('')
    # 公共-获取成交数据
    # result = spotAPI.get_deal(instrument_id='', limit='')
    # 公共-获取K线数据
    # result = spotAPI.get_kline(instrument_id='', start='', end='', granularity='')
    # 公共-获取历史K线数据
    # result = spotAPI.get_history_kline(instrument_id='', start='', end='', granularity='')

# level api test
# 币币杠杆API
    levelAPI = lever.LeverAPI(api_key, secret_key, passphrase, False)
    # 币币杠杆账户信息
    # result = levelAPI.get_account_info()
    # 单一币对账户信息
    # result = levelAPI.get_specific_account('')
    # 账单流水查询
    # result = levelAPI.get_ledger_record(instrument_id='', after='', before='', limit='', type='')
    # 杠杆配置信息
    # result = levelAPI.get_config_info()
    # 某个杠杆配置信息
    # result = levelAPI.get_specific_config_info('')
    # 获取借币记录
    # result = levelAPI.get_borrow_coin(status='', after='', before='', limit='')
    # 某币对借币记录
    # result = levelAPI.get_specific_borrow_coin(instrument_id='', status='', after='', before='', limit='')
    # 借币
    # result = levelAPI.borrow_coin(instrument_id='', currency='', amount='', client_oid='')
    # 还币
    # result = levelAPI.repayment_coin(instrument_id='', currency='', amount='', borrow_id='', client_oid='')
    # 下单
    # result = levelAPI.take_order(instrument_id='', side='', margin_trading='', client_oid='', type='', order_type='0', price='', size='', notional='')
    # 批量下单
    # result = levelAPI.take_orders([
    #     {'instrument_id': '', 'side': '', 'price': '', 'size': '', 'margin_trading': '2'},
    #     {'instrument_id': '', 'side': '', 'price': '', 'size': '', 'margin_trading': '2'}
    # ])
    # 撤销指定订单
    # result = levelAPI.revoke_order(instrument_id='', order_id='', client_oid='')
    # 批量撤销订单
    # result = levelAPI.revoke_orders([
    #     {'instrument_id': '', 'order_ids': ['', '']},
    #     {'instrument_id': '', 'client_oids': ['', '']}
    # ])
    # 获取订单列表
    # result = levelAPI.get_order_list(instrument_id='', state='', after='', before='', limit='')
    # 获取订单信息
    # result = levelAPI.get_order_info(instrument_id='', order_id='', client_oid='')
    # 获取所有未成交订单
    # result = levelAPI.get_order_pending(instrument_id='', after='', before='', limit='')
    # 获取成交明细
    # result = levelAPI.get_fills(instrument_id='', order_id='', after='', before='', limit='')
    # 获取杠杆倍数
    # result = levelAPI.get_leverage('')
    # 设置杠杆倍数
    # result = levelAPI.set_leverage(instrument_id='', leverage='')
    # 公共-获取标记价格
    # result = levelAPI.get_mark_price('')

# future api test
# 交割合约API
    futureAPI = future.FutureAPI(api_key, secret_key, passphrase, False)
    # 所有合约持仓信息
    # result = futureAPI.get_position()
    # 单个合约持仓信息
    # result = futureAPI.get_specific_position('')
    # 所有币种合约账户信息
    # result = futureAPI.get_accounts()
    # 单个币种合约账户信息
    # result = futureAPI.get_coin_account('')
    # 获取合约币种杠杆倍数
    # result = futureAPI.get_leverage('')
    # 设定合约币种杠杆倍数
    # 全仓
    # result = futureAPI.set_leverage(underlying='', leverage='')
    # 逐仓
    # result = futureAPI.set_leverage(underlying='', leverage='', instrument_id='', direction='')
    # 账单流水查询
    # result = futureAPI.get_ledger(underlying='', after='', before='', limit='', type='')
    # 下单
    # result = futureAPI.take_order(instrument_id='', type='', price='', size='', client_oid='', order_type='0', match_price='0')
    # 批量下单
    # result = futureAPI.take_orders('', [
    #     {'client_oid': '', 'type': '', 'price': '', 'size': '', 'match_price': '0'},
    #     {'client_oid': '', 'type': '', 'price': '', 'size': '', 'match_price': '0'}
    # ])
    # 撤销指定订单
    # result = futureAPI.revoke_order(instrument_id='', order_id='', client_oid='')
    # 批量撤销订单
    # result = futureAPI.revoke_orders(instrument_id='', order_ids=['', ''])
    # 修改订单
    # result = futureAPI.amend_order(instrument_id='', cancel_on_fail='', order_id='', client_oid='', request_id='', new_size='', new_price='')
    # 批量修改订单
    # result = futureAPI.amend_batch_orders(instrument_id='', amend_data=[
    #     {'cancel_on_fail': '', 'order_id': '', 'client_oid': '', 'request_id': '', 'new_size': '', 'new_price': ''},
    #     {'cancel_on_fail': '', 'order_id': '', 'client_oid': '', 'request_id': '', 'new_size': '', 'new_price': ''}
    # ])
    # 获取订单列表
    # result = futureAPI.get_order_list(instrument_id='', state='', after='', before='', limit='')
    # 获取订单信息
    # result = futureAPI.get_order_info(instrument_id='', order_id='', client_oid='')
    # 获取成交明细
    # result = futureAPI.get_fills(instrument_id='', order_id='', after='', before='', limit='')
    # 设置合约币种账户模式
    # result = futureAPI.set_margin_mode(underlying='', margin_mode='')
    # 市价全平
    # result = futureAPI.close_position(instrument_id='', direction='')
    # 撤销所有平仓挂单
    # result = futureAPI.cancel_all(instrument_id='', direction='')
    # 获取合约挂单冻结数量
    # result = futureAPI.get_holds_amount('')
    # 委托策略下单
    # result = futureAPI.take_order_algo(instrument_id='', type='', order_type='', size='', trigger_price='', algo_price='', algo_type='')
    # 委托策略撤单
    # result = futureAPI.cancel_algos(instrument_id='', algo_ids=[''], order_type='')
    # 获取委托单列表
    # result = futureAPI.get_order_algos(instrument_id='', order_type='', status='', algo_id='', before='', after='', limit='')
    # 获取当前手续费费率
    # result = futureAPI.get_trade_fee()
    # 增加/减少保证金
    # result = futureAPI.change_margin(instrument_id='', direction='', type='', amount='')
    # 设置逐仓自动增加保证金
    # result = futureAPI.set_auto_margin(underlying='', type='')
    # 公共-获取合约信息
    # result = futureAPI.get_products()
    # 公共-获取深度数据
    # result = futureAPI.get_depth(instrument_id='', size='', depth='')
    # 公共-获取全部ticker信息
    # result = futureAPI.get_ticker()
    # 公共-获取某个ticker信息
    # result = futureAPI.get_specific_ticker('')
    # 公共-获取成交数据
    # result = futureAPI.get_trades(instrument_id='', after='', before='', limit='')
    # 公共-获取K线数据
    # result = futureAPI.get_kline(instrument_id='', start='', end='', granularity='')
    # 公共-获取指数信息
    # result = futureAPI.get_index('')
    # 公共-获取法币汇率
    # result = futureAPI.get_rate()
    # 公共-获取预估交割价
    # result = futureAPI.get_estimated_price('')
    # 公共-获取平台总持仓量
    # result = futureAPI.get_holds('')
    # 公共-获取当前限价
    # result = futureAPI.get_limit('')
    # 公共-获取标记价格
    # result = futureAPI.get_mark_price('')
    # 公共-获取强平单
    # result = futureAPI.get_liquidation(instrument_id='', status='', limit='', froms='', to='')
    # 公共-获取历史结算/交割记录
    # result = futureAPI.get_history_settlement(instrument_id='', underlying='', start='', limit='', end='')
    # 公共-获取历史K线数据
    # result = futureAPI.get_history_kline(instrument_id='', start='', end='', granularity='')

# swap api test
# 永续合约API
    swapAPI = swap.SwapAPI(api_key, secret_key, passphrase, False)
    # 所有合约持仓信息
    # result = swapAPI.get_position()
    # 单个合约持仓信息
    # result = swapAPI.get_specific_position('')
    # 所有币种合约账户信息
    # result = swapAPI.get_accounts()
    # 单个币种合约账户信息
    # result = swapAPI.get_coin_account('')
    # 获取某个合约的用户配置
    # result = swapAPI.get_settings('')
    # 设定某个合约的杠杆
    # result = swapAPI.set_leverage(instrument_id='', leverage='', side='')
    # 账单流水查询
    # result = swapAPI.get_ledger(instrument_id='', after='', before='', limit='', type='')
    # 下单
    # result = swapAPI.take_order(instrument_id='', type='', price='', size='', client_oid='', order_type='0', match_price='0')
    # 批量下单
    # result = swapAPI.take_orders('', [
    #     {'client_oid': '', 'type': '', 'price': '', 'size': ''},
    #     {'client_oid': '', 'type': '', 'price': '', 'size': ''}
    # ])
    # 撤单
    # result = swapAPI.revoke_order(instrument_id='', order_id='', client_oid='')
    # 批量撤单
    # result = swapAPI.revoke_orders(instrument_id='', ids=['', ''], client_oids=['', ''])
    # 修改订单
    # result = swapAPI.amend_order(instrument_id='', cancel_on_fail='', order_id='', client_oid='', request_id='', new_size='', new_price='')
    # 批量修改订单
    # result = swapAPI.amend_batch_orders(instrument_id='', amend_data=[
    #     {'cancel_on_fail': '', 'order_id': '', 'client_oid': '', 'request_id': '', 'new_size': '', 'new_price': ''},
    #     {'cancel_on_fail': '', 'order_id': '', 'client_oid': '', 'request_id': '', 'new_size': '', 'new_price': ''}
    # ])
    # 获取所有订单列表
    # result = swapAPI.get_order_list(instrument_id='', state='', after='', before='', limit='')
    # 获取订单信息
    # result = swapAPI.get_order_info(instrument_id='', order_id='', client_oid='')
    # 获取成交明细
    # result = swapAPI.get_fills(instrument_id='', order_id='', after='', before='', limit='')
    # 获取合约挂单冻结数量
    # result = swapAPI.get_holds_amount('')
    # 委托策略下单
    # result = swapAPI.take_order_algo(instrument_id='', type='', order_type='', size='', trigger_price='', algo_price='', algo_type='')
    # 委托策略撤单
    # result = swapAPI.cancel_algos(instrument_id='', algo_ids=[''], order_type='')
    # 获取委托单列表
    # result = swapAPI.get_order_algos(instrument_id='', order_type='', status='', algo_id='', before='', after='', limit='')
    # 获取账户手续费费率
    # result = swapAPI.get_trade_fee()
    # 市价全平
    # result = swapAPI.close_position(instrument_id='', direction='')
    # 撤销所有平仓挂单
    # result = swapAPI.cancel_all(instrument_id='', direction='')
    # 公共-获取合约信息
    # result = swapAPI.get_instruments()
    # 公共-获取深度数据
    # result = swapAPI.get_depth(instrument_id='', size='', depth='')
    # 公共-获取全部ticker信息
    # result = swapAPI.get_ticker()
    # 公共-获取某个ticker信息
    # result = swapAPI.get_specific_ticker('')
    # 公共-获取成交数据
    # result = swapAPI.get_trades(instrument_id='', after='', before='', limit='')
    # 公共-获取K线数据
    # result = swapAPI.get_kline(instrument_id='', start='', end='', granularity='')
    # 公共-获取指数信息
    # result = swapAPI.get_index('')
    # 公共-获取法币汇率
    # result = swapAPI.get_rate()
    # 公共-获取平台总持仓量
    # result = swapAPI.get_holds('')
    # 公共-获取当前限价
    # result = swapAPI.get_limit('')
    # 公共-获取强平单
    # result = swapAPI.get_liquidation(instrument_id='', status='', froms='', to='', limit='')
    # 公共-获取合约资金费率
    # result = swapAPI.get_funding_time('')
    # 公共-获取合约标记价格
    # result = swapAPI.get_mark_price('')
    # 公共-获取合约历史资金费率
    # result = swapAPI.get_historical_funding_rate(instrument_id='', limit='')
    # 公共-获取历史K线数据
    # result = swapAPI.get_history_kline(instrument_id='', start='', end='', granularity='')

# option api test
# 期权合约API
    optionAPI = option.OptionAPI(api_key, secret_key, passphrase, False)
    # 单个标的指数持仓信息
    # result = optionAPI.get_specific_position(underlying='', instrument_id='')
    # 单个标的物账户信息
    # result = optionAPI.get_underlying_account('')
    # 下单
    # result = optionAPI.take_order(instrument_id='', side='', price='', size='', client_oid='', order_type='0', match_price='0')
    # 批量下单
    # result = optionAPI.take_orders('', [
    #     {'instrument_id': '', 'side': '', 'price': '', 'size': '', 'order_type': '0', 'match_price': '0'},
    #     {'instrument_id': '', 'side': '', 'price': '', 'size': '', 'order_type': '0', 'match_price': '0'}
    # ])
    # 撤单
    # result = optionAPI.revoke_order(underlying='', order_id='', client_oid='')
    # 批量撤单
    # result = optionAPI.revoke_orders(underlying='', order_ids=['', ''], client_oids=['', ''])
    # 修改订单
    # result = optionAPI.amend_order(underlying='', order_id='', client_oid='', request_id='', new_size='', new_price='')
    # 批量修改订单
    # result = optionAPI.amend_batch_orders('', [
    #     {'order_id': '', 'new_size': ''},
    #     {'client_oid': '', 'request_id': '', 'new_size': ''}
    # ])
    # 获取单个订单状态
    # result = optionAPI.get_order_info(underlying='', order_id='', client_oid='')
    # 获取订单列表
    # result = optionAPI.get_order_list(underlying='', state='', instrument_id='', after='', before='', limit='')
    # 获取成交明细
    # result = optionAPI.get_fills(underlying='', order_id='', instrument_id='', after='', before='', limit='')
    # 获取账单流水
    # result = optionAPI.get_ledger(underlying='', after='', before='', limit='')
    # 获取手续费费率
    # result = optionAPI.get_trade_fee()
    # 公共-获取标的指数
    # result = optionAPI.get_index()
    # 公共-获取期权合约
    # result = optionAPI.get_instruments(underlying='', delivery='', instrument_id='')
    # 公共-获取期权合约详细定价
    # result = optionAPI.get_instruments_summary(underlying='', delivery='')
    # 公共-获取单个期权合约详细定价
    # result = optionAPI.get_option_instruments_summary(underlying='', instrument_id='')
    # 公共-获取深度数据
    # result = optionAPI.get_depth(instrument_id='', size='')
    # 公共-获取成交数据
    # result = optionAPI.get_trades(instrument_id='', after='', before='', limit='')
    # 公共-获取某个Ticker信息
    # result = optionAPI.get_specific_ticker('')
    # 公共-获取K线数据
    # result = optionAPI.get_kline(instrument_id='', start='', end='', granularity='')
    # 公共-获取历史结算/行权记录
    # result = optionAPI.get_history_settlement(instrument_id='', start='', end='', limit='')

# information api test
# 合约交易数据API
    informationAPI = information.InformationAPI(api_key, secret_key, passphrase, False)
    # 公共-多空持仓人数比
    # result = informationAPI.get_long_short_ratio(currency='', start='', end='', granularity='')
    # 公共-持仓总量及交易量
    # result = informationAPI.get_volume(currency='', start='', end='', granularity='')
    # 公共-主动买入卖出情况
    # result = informationAPI.get_taker(currency='', start='', end='', granularity='')
    # 公共-多空精英趋向指标
    # result = informationAPI.get_sentiment(currency='', start='', end='', granularity='')
    # 公共-多空精英平均持仓比例
    # result = informationAPI.get_margin(currency='', start='', end='', granularity='')

# index api test
# 指数API
    indexAPI = index.IndexAPI(api_key, secret_key, passphrase, False)
    # 公共-获取指数成分
    # result = indexAPI.get_index_constituents('')

# system api test
# 获取系统升级状态
    system = system.SystemAPI(api_key, secret_key, passphrase, False)
    # 公共-获取系统升级状态
    # result = system.get_system_status('')


    print(time + json.dumps(result))