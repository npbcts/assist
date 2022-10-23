#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 16: 29
# @Author  :Jason
# @Site   : www.auditor.ren
# @File   : 用于读写json文件数据函数集合
# @Software  : Vscode

import json


def save_json(data_dic, filename: str, encoding='utf-8') -> None:
    """
    将字典格式数据作为文件保存至程序文件夹
    """
    with open(filename, 'w', encoding=encoding) as f:
        json.dump(data_dic, f, ensure_ascii=False)


def read_json(filename_json: str, mode='r', encoding='utf-8'):
    '''
    本函数用于读取json文件。

    Parameters
    ----------
    filename_json : 字符串(str)
        DESCRIPTION.读取的json文件地址

    Returns
    -------
    json_data : dict,list等json支持的数据格式
    '''
    with open(filename_json, mode=mode, encoding=encoding) as f:
        json_data = json.load(f)
    return json_data
