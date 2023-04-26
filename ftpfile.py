
import os
from ftplib import FTP
from typing import Union
from logging import Logger


class FtpDownUpFile():
    """
    通过ftp的方式, 下载和上传远程服务器上的文件
    """
    def __init__(self, host: str, username: str, password: str, logger: Union[Logger, None] = None) -> None:
        """创建ftp服务器,也是对外接口

            默认本地文件和ftp中的文件名称相同

        Args:
            host (str): ftp的ip地址
            username (str): ftp用户名
            password (str): ftp密码
            logger (Union[Logger, None]): 可以传入一个日志记录器

        Returns:
            FTP: ftp服务器连接实例
        """
        FTP.encoding = 'utf-8'  # 源码 encoding 'latin-1' error
        self.ftp = FTP(host, user=username, passwd=password)
        connect_welcome = self.ftp.getwelcome()
        self.logger = logger
        faild_str = f"faild to connect ftp host: {host}, username: {username}, password: {password}"
        self._logger(connect_welcome)
        assert connect_welcome[:1] == "2", faild_str

    def _logger(self, response):
        if response[:1] == '2':
            if self.logger is not None:
                self.logger.info(f"Success {response}")
        else:
            if self.logger is not None:
                self.logger.error(f"Faild {response}")

    def downloadfile(self, remotepath: str, localpath: str, filename: str) -> str:
        """从ftp服务器下载文件

        Args:
            remotepath (str): 远程(复制源)文件夹
            localpath (str): 本地文件夹
            filename (str): 需要复制到本地的文件名
        Returns:
            str: 下载详细情况的字符串
        """
        download_info = 'copyfile from {} --> {}, file is {}'.format(remotepath, localpath, filename)
        if self.logger is not None:
            self.logger.info(f"Begin { download_info }")
        bufsize = 1024
        self.ftp.cwd(remotepath)
        fp = open(os.path.join(localpath, filename), 'wb')
        response_code = self.ftp.retrbinary('RETR %s' % os.path.basename(filename), fp.write, bufsize)
        self._logger(response_code)
        fp.close()
        return response_code

    def uploalfile(self, remotepath: str, localpath: str, filename: str) -> str:
        """
        uploalfile 将本地文件上传至ftp服务器

            默认本地文件和ftp中的文件名称相同

        Args:
            remotepath (str): 服务器(上传目标)文件夹。
                注意服务器为linux末尾加斜杠'/',路径拼接成linux路径; 反之既然。
            localpath (str): 本地文件夹, 包含要上传的文件
            filename (str): 要上传的文件名

        Returns:
            str: 上传详细情况的字符串
        """
        upload_info = 'upload from {} --> {}, file is {}'.format(localpath, remotepath, filename)
        if self.logger is not None:
            self.logger.info(f"Begin { upload_info }")
        bufsize = 1024
        local_filepath = os.path.join(localpath, filename)
        fp = open(local_filepath, 'rb')
        remote_filepath = os.path.join(remotepath, filename)
        response_code = self.ftp.storbinary('STOR ' + remote_filepath, fp, bufsize)
        self._logger(response_code)
        return response_code


if __name__ == "__main__":
    from assist.mylogger import get_logger
    logger = get_logger('ftpfile', '.')
    dellftp = FtpDownUpFile("192.168.2.141", "chloe", "20200415", logger)
    localpath = './'
    remotepath = '~/temp/'
    filename = "README.md"
    dellftp.uploalfile(remotepath, localpath, filename)
    localpath = '..'
    dellftp.downloadfile(remotepath, localpath, filename)
