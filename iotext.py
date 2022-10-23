#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 16: 29
# @Author  :Jason
# @Site   : www.auditor.ren
# @File   : 用于读写文件数据函数集合
# @Software  : Vscode


def save_text(text, filename, mode='w', encoding='utf-8'):
    with open(filename, mode=mode, encoding=encoding) as f:
        f.write(text)
        f.close()


def read_text(filename, mode='r', encoding='utf8'):
    with open(filename, mode=mode, encoding=encoding) as f:
        text = f.read()
    return text
