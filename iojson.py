#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 16: 29
# @File   : 用于读写json文件数据函数集合
# @Software  : Vscode
import os
import json
import logging
from typing import Dict, Any


def save_json(data_dic: Dict[Any, Any], filename: str, encoding='utf-8') -> None:
    #
    """
    save_json 将字典格式数据作为文件保存至程序文件夹

    Args:
        data_dic (Dict[Any, Any]): python 字典格式数据
        filename (str): 保存json文件
        encoding (str, optional): 保存coding. Defaults to 'utf-8'.
    """    
    if not os.path.exists(filename):
        logging.info(f'have no find {filename}, please check path!')
        return
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
    if not os.path.exists(filename_json):
        logging.info(f'have no find {filename_json}, please check path!')
        return
    with open(filename_json, mode=mode, encoding=encoding) as f:
        json_data = json.load(f)
    return json_data
