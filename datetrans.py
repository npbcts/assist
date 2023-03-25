from os import path
import re
from datetime import datetime
from iojson import read_json
this_path = path.abspath(path.dirname(__file__))


def chinese2digitdate(day_ch):
    """
    中文日期转化为数字日期
    例如：二零二一年十二月三十一日，转换成->2021年12月31日
    """
    if not day_ch:
        return ''
    year = day_ch.split('年')[0]
    month = day_ch.split('年')[1].split('月')[0]
    day = day_ch.split('年')[1].split('月')[1].split('日')[0]
    # 去掉"日"中的十,例如"三十一"转化为"三一"
    if len(day) > 2:
        day = day[0] + day[2]
    # 构建对应数字转换字典
    # NUM = {'〇': 0, '○': 0, '零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}
    NUM = read_json(path.join(this_path, 'data_hash_config.json'))
    # 利用join对查找到的值进行连接
    year = ''.join(str(NUM[i]) for i in year)
    month = ''.join(str(NUM[i]) for i in month)
    day = ''.join(str(NUM[i]) for i in day)
    # 月处理(例如"十二"月转换为"102",只取"1"和"2")
    if len(month) == 3:
        month = '1' + month[2]
    # 日处理(例如"二十"日转换为"210",只取"2"和"0")
    if len(day) == 3:
        day = day[0] + day[2]
    # 将各部分进行拼接组合
    new_date = (year + '年' + month + '月' + day + '日')
    return new_date


def chinese2date(date_str):
    """
    文字型日期('X年X月X日')转换为python日期数据(datetime)
    """
    if date_str is None:
        return None
    the_date_date = None
    re_pattern = re.compile(r'(\d+)\D+(\d+)\D+(\d+)\D*')
    if re_pattern.match(date_str):
        results = re_pattern.findall(date_str)
    else:
        results = re_pattern.findall(chinese2digitdate(date_str))
    if results:
        theyear, themonth, theday = results[0]
        the_date_date = datetime(int(theyear), int(themonth), int(theday))
    return the_date_date
