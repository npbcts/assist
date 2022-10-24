import zipfile
import os
from typing import List
import logging


def zip_files(files: List[str], zip_name: str) -> None:
    """
    zip_files 使用zipfile包形成系列文件的压缩包

    Args:
        files (List[str]): 包含文件名(含路径)的列表
        zip_name (str): 打包文件名(含路径)
    """    
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        if not os.path.exists(file):
            logging.info(f'have no find {file}, please check path!')
            continue
        logging.info('compressing', file)
        zip.write(file)
    zip.close()
    logging.info('compressing finished')