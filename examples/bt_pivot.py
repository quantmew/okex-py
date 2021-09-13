# -*- coding:utf-8 -*-
#
# Copyright (c) 2021 Hundsun.com, Inc. All Rights Reserved
#
"""
这个模块提供了支撑阻力策略
@FileName  :  pivot_point.py
@Author    :  yujl
@Time      :  2021/4/21 13:26
"""

import backtrader as bt

class PivotStrategy(bt.Strategy):
    """支撑阻力策略
    《151 Trading Strategies》P51
    支撑阻力策略实现
    支撑阻力策略计算支撑线和阻力线：
    中心线：C = (P_H + P_L + P_C) / 3
    阻力线：R = 2 * C - P_L
    支撑线：S = 2 * C - P_H
    注：P_H, P_L和P_C分别是前一天的最高价、最低价和收盘价
    价格穿越阻力线，卖出；价格穿越支撑线，买入
    Attributes:
        close: 收盘价
    """
    def __init__(self):
        self.order = None
        self.close = self.data.close
    
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if self.order is not None:
             return

        pre_high = self.data.high[-1]
        pre_low = self.data.low[-1]
        pre_close = self.data.close[-1]

        p_p = (pre_low + pre_high + pre_close) / 3.0
        p_r = 2 * p_p - pre_low
        p_s = 2 * p_p - pre_high

        if not self.position:
            if self.close[0] >= p_r:
                self.order = self.sell()
        else:
            if self.close[0] <= p_s:
                self.order = self.buy()