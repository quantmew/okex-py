# -*- coding:utf-8 -*-
#
# Copyright (c) 2021 Hundsun.com, Inc. All Rights Reserved
#
"""
这个模块提供了凯特勒通道策略
@FileName  :  ketler.py
@Author    :  yujl
@Time      :  2021/4/21 10:37
"""

import backtrader as bt

class KetlerStrategy(bt.Strategy):
    """凯特勒通道策略
    https://zhuanlan.zhihu.com/p/345415058
    凯特勒通道计算公式如下：
    凯特勒通道中线 = EMA(exponential moving average)
    凯特勒通道上线 = EMA + n * ATR(average true range)
    凯特勒通道下线 = EMA - n * ATR
    注：n可以为任何正整数，一般取2，这里用的是1
    价格穿越上线，买入；穿越中线，卖出
    Attributes:
        expo: 通道中线
        atr: 真实波幅均值
        upper: 通道上线
        lower: 通道下线
    """
    params = (('ema_period', 20), ('atr_period', 17))

    def __init__(self):
        print("ema_period: ", self.params.ema_period)
        print("atr_period: ", self.params.atr_period)
        self.expo = bt.talib.EMA(self.datas[0].close, timeperiod=self.params.ema_period)
        self.atr = bt.talib.ATR(self.data.high, self.data.low, self.data.close, timeperiod=self.params.atr_period)
        self.upper = self.expo + self.atr
        self.lower = self.expo - self.atr
        self.close = self.data.close
    
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        # 如果已经下单，则返回
        if self.order:
            return

        # 是否已买入
        if not self.position:
            # 没有买入，如果收盘价>上线，表示股票涨势，买入
            if self.close[0] > self.upper[0]:
                self.order = self.order_target_percent(target=0.95)
        else:
            # 已经买了，如果收盘价<中线，表示股票跌势，卖出
            if self.close[0] < self.expo[0]:
                self.order = self.sell()
