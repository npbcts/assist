import random
import string


def get_random_char(n: int, symbol: bool = False) -> str:
    """
    get_random_char 生成给定数量的随机字符串

    Args:
        n (int): 生成随机字符串的数量
        symbol (bool, optional): 是否包含符号， "!@#$%^&*()-+=.". Defaults to False.

    Returns:
        str: 随机字符串
    """
    random_chars = []
    sample = random.sample(string.ascii_letters + string.digits, 62)  # 从a-zA-Z0-9生成指定数量的随机字符： list类型
    if symbol is True:
        sample = sample + list('!@#$%^&*()-+=.')  # 原基础上加入一些符号元素
    for i in range(n):
        char = random.choice(sample)  # 从sample中选择一个字符
        random_chars.append(char)
    return ''.join(random_chars)  # 返回字符串
