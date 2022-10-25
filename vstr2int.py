#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 16: 29
# @File   : 文本型(str)版本号转为数字型(int)
# @Software  : Vscode
from typing import Union
import logging


def version_str2int(the_version_str: str) -> Union[int, None]:
    """
    version_str2int 字符串类型版本号转化为数字型

    Args:
        the_version_str (str): 表示版本号的字符串, e.g: '22.10.4.0'

    Returns:
        int, None: 返回数字化的版本号 或者 None
    """
    if not the_version_str or not isinstance(the_version_str, str):
        logging.info('please input correct version_str')
        return None
    return int(''.join(the_version_str.split('.')))
