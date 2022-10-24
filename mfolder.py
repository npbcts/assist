import os
import shutil
import logging


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
            logging.info(f'set "rebuild == True” for del and creat new folder')
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