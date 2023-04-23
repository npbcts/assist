
"""
@descript 匈牙利: 变量名=属性+类型+对象描述; 属性(小写字母+_)<：g_:全局变量; m_:类成员变量; s_:静态变量; c_:常量;> 类型：<b:bool; sz:以零结束的字符串; p:指针; n:整整; dw:双字; l:长整型; 无符号:u; 函数:fn>
@descript 帕斯卡: 命名中的每一个逻辑断点（单词）都用大写字母标记,同大驼峰
@descript 大驼峰: 首字母大写其余每一个逻辑断点（单词）都用大写字母标记,同帕斯卡
@descript 小驼峰: 首字母小写其余每一个逻辑断点（单词）都用大写字母标记
@descript 下划线: 逻辑断点（单词）用的是下划线隔开
"""
import re


class RuleConvert:
    """
    命名规则转换 Tips:大小驼峰及下划线互转
    @descript 大驼峰: 首字母大写其余每一个逻辑断点（单词）都用大写字母标记,同帕斯卡命名法
    @descript 小驼峰: 首字母小写其余每一个逻辑断点（单词）都用大写字母标记
    @descript 下划线: 逻辑断点（单词）用的是下划线隔开
    """

    @staticmethod
    def to_Underline(x):
        """转下划线命名"""
        return re.sub('(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])', '_\g<0>', x).lower()

    @staticmethod
    def to_upper_camel_case(x):
        """转大驼峰法命名"""
        s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x.lower())
        return s[0].upper() + s[1:]

    @staticmethod
    def to_lower_camel_case(x):
        """转小驼峰法命名"""
        s = re.sub('_([a-zA-Z])', lambda m: (m.group(1).upper()), x.lower())
        return s[0].lower() + s[1:]

if __name__ == "__main__":
    a = "USER_NAME"
    b = "UserNamepass"
    print(RuleConvert.to_Underline(a))
    print(RuleConvert.to_Underline(b))
    print(RuleConvert.to_upper_camel_case(a))
    print(RuleConvert.to_lower_camel_case(a))
