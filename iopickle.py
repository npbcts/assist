#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 16: 29
# @Author  :Jason
# @Site   : www.auditor.ren
# @File   : 用于读写pickle文件数据函数集合
# @Software  : Vscode

import pickle


def save_pickle(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def read_pickle(filename):
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    return obj
