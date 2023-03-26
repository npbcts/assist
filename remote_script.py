from typing import Tuple
import paramiko


# paramiko详细用法见 https://zhuanlan.zhihu.com/p/313718499
# paramiko功能较强，可以使用这个库向远程服务器发送linux命令或是ftp下载或者上传文件


class RemoteScript():
    """
    RemoteScript 使用ssh用户名及对应密码,本地执行远程服务器上的命令.
    """
    def __init__(self, hostname: str, username: str, password: str) -> None:
        # 创建SSH对象
        self.ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        self.ssh.connect(hostname=hostname, port=22, username=username, password=password)

    def __call__(self, cmd: str) -> Tuple[str, str]:
        """
        __call__ _summary_

        _extended_summary_

        Args:
            cmd (str): 命令执行字符串

        Returns:
            str: 命令执行结果的输出字符串
        """
        # 执行命令
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        # 获取命令结果
        result_stdout = stdout.read().decode('utf8')
        result_stderr = stderr.read().decode('utf8')
        if result_stdout:
            print(result_stdout)  # 被执行脚本会返回logger信息，此时再使用logger会使显示信息部分重复
        if result_stderr:
            logger.error(result_stderr)
        return result_stdout, result_stderr

    def __del__(self):
        # 关闭连接
        self.ssh.close()
