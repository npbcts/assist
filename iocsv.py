#!/usr/local/bin/python3.8
# -*- coding: utf-8 -*-
# @Time   : 2022/10/13 16: 29
# @File   : 使用pandas用于读写csv文件数据函数集合
# @Software  : Vscode
import pandas as pd


def save_dict_csv(data_dic, file_name, index=False):
    '''
    本函数用于将dict字典数据储存为csv文件

    Parameters
    ----------
    data_dic : 字典
        DESCRIPTION.需要储存的dict字典数据
    file_name : 字符串
        DESCRIPTION.储存目标文件名称

    Returns
    -------
    None.

    '''
    data_pd = pd.DataFrame(data_dic)
    data_pd = data_pd.T
    data_pd.to_csv(file_name, index=index)


def read_csv(file_name):
    data = pd.read_table(file_name, sep='/t', )
    return data
