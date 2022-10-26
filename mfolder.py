#!/usr/bin python3.8
# coding: utf-8
import os
import shutil
import logging
from typing import List


def mk_folder(folder: str, rebuild=False) -> None:
    """
    mk_folder 创建的文件夹，如果文件夹已存在，则删除再创建
    Args:
        folder (str): 需要创建的文件夹名称
    """
    if os.path.exists(folder):
        if rebuild == True:
            shutil.rmtree(folder)
        else:
            logging.info(f'folder {folder} exist, can`t creat new!')
            logging.info(f'you may set "rebuild == True" for del and creat new folder')
            return
    logging.info(f'folder {folder} create already!')
    os.mkdir(folder)
    


def rm_folder(folder: str) -> None:
    """
    rm_folder 直接删除文件夹

    Args:
        folder (str): 文件夹路径
    """    
    if os.path.exists(folder):
        shutil.rmtree(folder)
        logging.info(f'folder: {folder} deleted already!')
    else:
        logging.info(f'have no find {folder}, please check folder path!')


def files_2_folder(files: List[str], source_folder: str, aim_folder: str) -> None:
    """
    files_2_folder: 将source_folder中的文件复制到aim_folder文件夹。
    Args:
        files (List[str]): 脚本文件名的列表,不包含路径
        source_folder(str): 源文件夹, path like类型, 即文件夹路径
        aim_folder(str): 目标文件夹, path like类型, 即文件夹路径
    """
    log_str = 'can`t find folder {}, please check!'
    path_exist = True
    if not os.path.exists(source_folder):
        logging.info(log_str.format(source_folder))
        path_exist = False
    if not os.path.exists(aim_folder):
        logging.info(log_str.format(aim_folder))
        path_exist = False
    if not path_exist:
        return
    for file in files:
        source_file = os.path.join(source_folder, file)
        if not os.path.exists(source_file):
            logging.info(log_str.format(source_file))
            continue  # 需要复制的源文件不存在，进入复制文件的下一个循环
        shutil.copy(source_file, os.path.join(aim_folder, file))


def del_folder_files(files: List[str], aim_folder) -> None:
    """
    del_folder_files: 删除目标文件夹中文件。

    Args:
    files (List[str]): 文件名的列表,只有文件名，不包含路径
    aim_folder: 待删除文件所在的文件夹
    """
    for file in files:
        file_path = os.path.join(aim_folder, file)
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            logging.info(f"file {file_path} does not exist")

def copy_folder(source_path, target_path):
    if not os.path.exists(target_path):
        # 如果目标路径不存在原文件夹的话就创建
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # 如果目标路径存在原文件夹的话就先删除
        shutil.rmtree(target_path)

    shutil.copytree(source_path, target_path)
    logging.info(f'copy folder {source_path} -> {target_path}')
