# -*- coding:utf-8 -*-
#
# Copyright (c) 2021 Hundsun.com, Inc. All Rights Reserved
#
"""
这个模块提供了价格动量策略
@FileName  :  price_rate_change.py
@Author    :  yujl
@Time      :  2021/4/21 13:13
"""
import pandas as pd
import backtrader as bt


class PriceMomentumStrategy(bt.Strategy):
    """价格动量策略
    《151 Trading Strategies》P40
    价格动量策略实现
    计算公式：R_cum = (Price - PrePrice) / PrePrice
    R_cum > 0, 买入；R_cum < 0, 卖出
    Attributes:
        proc: 价格动量
    """
    params = (('time_period', 20),)

    def __init__(self):
        self.order = None
        print('time period:', self.params.time_period)
        self.proc = bt.talib.ROCP(self.datas[0].close, timeperiod=self.params.time_period)

    def next(self):
        if self.order is not None:
            return
        if not self.position:
            # 没有买入，如果价格动量大于零，表示股票涨势，买入
            if self.proc[0] > self.proc[1]:
                self.order = self.buy()  # (target=0.90)
        else:
            # 已经买入，如果价格动量小于零，表示股票跌势，卖出
            if self.proc[0] < 0:
                self.order = self.sell()

