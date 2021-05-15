#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project  : crypto
# @Time     : 2021/4/21 9:26
# @Author   : Adolf
# @File     : two_sma.py
# @Function  :

import backtrader as bt
import pandas as pd


class TwoSmaStrategy(bt.Strategy):
    """双均线策略
    《151 Trading Strategies》P50
    需要计算两类均值：短周期均值和长周期均值。当短周期均值穿过长周期均值买入，否则卖出
    Attributes:
        sma5: 短周期均值
        sma10: 长周期均值
    """
    params = (('short_period', 20), ('long_period', 40))

    def __init__(self):
        super(TwoSmaStrategy, self).__init__()
        self.order = None
        self.sma_short = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.short_period)
        self.sma_long = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.long_period)
        self.crossover_sma = bt.ind.CrossOver(self.sma_short, self.sma_long)

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        # self.log('Open,%.2f' % self.datas[0].open[0])
        # self.log('Close, %.2f' % self.data_close[0])
        # self.log(self.position.size, doprint=True)

        # if self.order is not None:
        #     return

        if self.crossover_sma > 0:
            # buy_size = int(self.broker.getcash() / self.data_close[0]) - 1
            # now_cash = self.broker.getcash()
            # now_price = self.data_close[0]

            # self.log("应该所剩余额:{}".format(now_cash - now_price * buy_size), doprint=True)
            # self.log("目前是买点,目前拥有的现金:{},目前的收盘价是:{},买入份额:{},手续费:{}".format(now_cash, now_price,
            #                                                              buy_size,
            #                                                              self.buy_comm),
            #          doprint=True)
            # self.log("购买时的价格：{}".format(self.datas[0].open[1]))
            self.order = self.buy(size=(int(self.broker.getcash() / self.datas[0].open[0])))
            # print(self.order)
        else:
            if self.crossover_sma < 0:
                # self.log("卖出前:{}".format(self.position.size))
                self.order = self.sell(size=self.position.size)