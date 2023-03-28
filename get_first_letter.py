#!/usr/bin/python3
# -*-encoding:utf-8-*-
import pinyin
from inspect import signature  # python3才有的模块


def check_type(*ty_args, **ty_kwargs):
    """
    check_type 装饰器: 验证函数输入的参数是否为给定的数据类型,如果不是,抛出类型异常
    """
    def out_wrapper(func):
        # 通过signature方法，获取函数形参：name, age, height
        sig = signature(func)
        # 获得装饰器传来的参数， 函数签名与之绑定，字典类型
        bind_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        # print(bind_types)

        def wrapper(*args, **kwargs):
            # 给执行函数中具体的实参进行和形参进行绑定，形成字典的形式
            func_type = sig.bind(*args, **kwargs).arguments.items()
            # print(func_type)
            # 循环形参和实参字典的items()形式
            for name, obj in func_type:
                if name in bind_types:
                    if not isinstance(obj, bind_types[name]):
                        raise TypeError('%s must be %s' % (name, bind_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return out_wrapper


@check_type(str)
def get_first_letter(han_characters: str) -> str:
    """
    get_first_letter 输入汉字字符串，返回字符串的首字母

    Args:
        han_characters (str): 汉字字符串

    Returns:
        str: 汉字字符串中首字母组成的字符串
    """
    first_letters = ''
    for han_character in han_characters:
        first_letter = pinyin.get(han_character)[0]
        first_letters += first_letter
    return first_letters
