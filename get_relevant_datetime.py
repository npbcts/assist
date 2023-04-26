import datetime


def get_last_day(days: int) -> datetime.date:
    """
    get_lastday 获取今天之前的某一天日期

    Args:
        days (int): 今天之前的天数

    Returns:
        datetime.date: 日期类型数据
    """
    today = datetime.date.today()
    lastdays_delta = datetime.timedelta(days=days)
    last_day = today - lastdays_delta
    return last_day


def get_last_year(years: int) -> int:
    """
    get_last_Year 获取当前年度的前几个年度

    Args:
        years (int): 年数

    Returns:
        int: 前几个年度的年数
    """
    now = datetime.datetime.now()
    last_year = int(now.year) - years
    return last_year


if __name__ == '__main__':
    print(get_last_day(1))
    print(get_last_year(1))
