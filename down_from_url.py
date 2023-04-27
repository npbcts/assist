import requests
import os
from typing import Union, Tuple
from logging import Logger

HEADER = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    "Content-Type": "application/json; charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
    "Connection": "keep-alive",
    }


def down_from_url(file_url: str, down_path: str, logger: Union[Logger, None] = None) -> Tuple[bool, str]:
    """
    down_from_url 下载网页链接中的文件

    Args:
        file_url (str): 下载文件的连接地址:e.g:
            'https://www.swsresearch.com/swindex/pdf/StockClassifyUse_stock.xls'
            'https://www.swsresearch.com/swindex/pdf/SwClass2021/SwClass.rar'
        down_path (str): 包含文件全路径名称(包含路径,文件名及扩展名)
        logger (Union[Logger, None]): 用于记录日志.可选。

    Returns:
        bool: 是否保存成功的布尔值
    """
    r = requests.get(file_url, headers=HEADER)
    file_size = 0
    if r.status_code == requests.codes.ok:
        # file_size = int(r.headers.get('Content-Length'))  #  返回不提供此字段
        with open(down_path, 'wb') as f:
            f.write(r.content)
    if os.path.exists(down_path) and os.path.getsize(down_path) > 500000:
        # 根据文件大小(例如0k文件)判断下载是否成功。
        save_result = True
        save_result_str = 'Success'
    else:
        save_result = False
        save_result_str = 'SaveFaild'
    if logger is not None:
        logger.info(f'{down_path} download compelete, {save_result_str}')

    return save_result, save_result_str
