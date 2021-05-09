
'''
Here is the okex api example.

'''

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

    with open('api.json', 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
    api_key = obj['api_key']
    secret_key = obj['secret_key']
    passphrase = obj['passphrase']

    # param use_server_time's value is False if is True will use server timestamp
    # param test's value is False if is True will use simulative trading

    # account api test
    # 资金账户API
    accountAPI = account.AccountAPI(api_key, secret_key, passphrase, False)
    # 查看账户持仓风险
    from okex.v5.insttype import InstType
    result = accountAPI.get_position_risk(instType=InstType.MARGIN)
    # print(result)

    # 查看账户余额
    from okex.v5.ccytype import CcyType
    result = accountAPI.get_balance(ccyType=CcyType.BTC)
    # print(result)

    # 查看持仓信息
    from okex.v5.insttype import InstType
    result = accountAPI.get_positions()
    # print(result)

    # 账单流水查询（近七天）
    result = accountAPI.get_bills()
    # print(result)

    # 账单流水查询（近三个月）
    result = accountAPI.get_bills_archive()
    # print(result)
