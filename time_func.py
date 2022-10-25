#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 17: 29
# @File   : 用于测量函数运行时间的装饰器
# @Software  : Vscode
import time
import logging
from functools import wraps


def time_func(func):
    # 使用wraps, 保证被装饰过的函数__name__的属性不变
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        logging.info('函数 {} 运行时间是 {} 毫秒'.format(func.__name__, (end_time - start_time)*1000))
        return res
    return inner
