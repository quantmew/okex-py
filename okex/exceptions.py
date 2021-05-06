#!/usr/bin/env python
#coding:utf-8

"""
将用户code导致的异常和系统内部异常使用两个异常基类区分（UserCodeError，InternalError）
"""


class UserCodeError(Exception):
    # 用户代码导致的相关异常
    pass


class InternalError(Exception):
    # qmdata内部的异常
    pass


class ParamsError(UserCodeError):
    # 用户传入的api参数不合理
    pass


class SecurityNotExist(UserCodeError):
    # 用户尝试使用标的列表中不存在的标的
    pass


class MissDataError(InternalError):
    # 数据缺失导致的异常
    pass


class InitObjError(InternalError):
    # 常用于初始化对象时由于内部错误（比如数据错误）抛出的异常
    pass


class InvalidDataError(InternalError):
    # 数据不正常抛出的异常（比如复权因子小于0）
    pass


class TimeoutError(InternalError):
    # 超时时触发的异常
    pass


class FutureDataError(UserCodeError):
    # 用户取未来数据时的异常
    pass