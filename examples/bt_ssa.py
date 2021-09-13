# -*- coding:utf-8 -*-
#
# Copyright (c) 2021 Hundsun.com, Inc. All Rights Reserved
#
"""
这个模块提供了奇异值分解策略
@FileName  :  ssa.py
@Author    :  yujl
@Time      :  2021/4/21 10:55
"""

import numpy as np
import backtrader as bt


class SSAIndicator(bt.Indicator):
    """奇异谱分析指标计算
    奇异谱分析是把股价组成一个n*m的矩阵
    x=（y1, y2, y3, ..., ym;
     y2, y3, y4, ..., ym+1;
     ....................
     ....................
     yn, yn+1, yn+2, ..., yT
    ）
    计算x.T * x，并进行奇异值分解，得到m个特征值，然后按照从大到小的原则进行矩阵重构
    Attributes:
        lines: 设置计算的指标
    """
    lines = ('ssa', )

    def __init__(self, ssa_window):
        """设置参数
        Args:
            ssa_window: ssa的窗口大小
        """
        self.params.ssa_window = ssa_window
        self.addminperiod(self.params.ssa_window * 2)

    def get_window_matrix(self, input_array, t, m):
        """将时间序列变成矩阵
        Args:
            input_array: 股价的时间序列
            t: 为时间序列长度
            m: 为矩阵列数
        Returns:
            价格矩阵
        """
        temp = []
        n = t - m + 1
        for i in range(n):
            temp.append(input_array[i:i+m])
        window_matrix = np.array(temp)

        return window_matrix

    # 奇异值分解
    def svd_reduce(self, window_matrix):
        u, s, v = np.linalg.svd(window_matrix)
        m1, n1 = u.shape
        m2, n2 = v.shape
        index = s.argmax()
        u1 = u[:, index]
        v1 = v[index]
        u1 = u1.reshape((m1, 1))
        v1 = v1.reshape((1, n2))
        value = s.max()
        new_matrix = value * (np.dot(u1, v1))
        return new_matrix

    # 时间序列重构
    def recreate_array(self, new_matrix, t, m):
        ret = []
        n = t - m + 1
        for p in range(1, t+1):
            if p < m:
                alpha = p
            elif p > t - m + 1:
                alpha = t - p + 1
            else:
                alpha = m
            sigma = 0
            for j in range(1, m+1):
                i = p - j + 1
                if i > 0 and i < n + 1:
                    sigma += new_matrix[i-1][j-1]
            ret.append(sigma / alpha)

        return ret

    def SSA(self, input_array, t, m):
        window_matrix = self.get_window_matrix(input_array, t, m)
        new_matrix = self.svd_reduce(window_matrix)
        new_array = self.recreate_array(new_matrix, t, m)

        return new_array

    def next(self):
        data_serial = self.data.get(size=self.params.ssa_window * 2)
        self.lines.ssa[0] = self.SSA(data_serial, len(data_serial), int(len(data_serial) / 2))[-1]


class SSAStrategy(bt.Strategy):
    """奇异值分解策略
    https://uqer.datayes.com/v3/community/share/577cbae4228e5b8a02931e1a
    收盘价大于重组后的值，买入；否则卖出
    Attributes:
        ssa: 奇异值分解指标对象
        dataclose: 收盘价
    """
    params = (('ssa_window', 15), )
    def __init__(self):
        self.order = None
        print("ssa_window: ", self.params.ssa_window)
        self.ssa = SSAIndicator(ssa_window=self.params.ssa_window)
        self.dataclose = self.datas[0].close
    
    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def next(self):
        if self.order is not None:
            return

        # 是否已买入
        if not self.position:
            # 没有买入，如果收盘价>奇异值，表示股票涨势，买入
            if self.dataclose[0] > self.ssa[0]:
                self.log('BUY CREATE, %.2f' % self.dataclose[0])

                self.order = self.buy()
        else:
            # 已经买了，如果收盘价<奇异值，表示股票跌势，卖出
            if self.dataclose[0] < self.ssa[0]:
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                self.order = self.sell()
