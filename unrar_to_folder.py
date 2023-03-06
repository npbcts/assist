from unrar import rarfile


def unrar_to_folder(therarfile: str, release_folder: str):
    """
    unrar_to_folder 解压rar压缩包,放在release_folder中

    Args:
        therarfile (str): 被解压文件
        release_folder (str): 解压后文件放置的目标文件夹
    """
    rf = rarfile.RarFile(therarfile, mode='r')
    rf.extractall(release_folder)


r"""
python程序解压rar压缩包报错
发布于2020-01-10 01:37:57阅读 3730
运行如下python程序报错Couldn't find path to unrar library的解决办法：

```
from unrar import rarfile
file = rarfile.RarFile('/root/ssl.rar')
file.extractall('/tmp')
```
复制
备注：rarfile已经通过pip3 install rarfile安装，但是unrar用pip3虽然提示成功但是有问题，所以手动安装下unrar包。

1. 安装依赖包

`yum install gcc gcc-c++`


2. 下载unrar包、安装、编译
```
wget http://www.rarlab.com/rar/unrarsrc-5.4.5.tar.gz
tar zxf unrarsrc-5.4.5.tar.gz
cd unrar
```

使用make lib命令将会自动编译库文件，再使用make install-lib命令产生 libunrar.so 文件（一般在 /usr/lib 目录下面）
```
make lib
make install-lib
```


3. 在/etc/profile文件末尾加上
```
vi /etc/profile
export UNRAR_LIB_PATH=/usr/lib/libunrar.so
```
成功保存后再使用命令使变量生效

`source /etc/profile`

4. windows下的使用

详细说明见: https://blog.csdn.net/Lilygjy/article/details/118514265

    安装步骤：
    1. 官网下载 

    RARLab官方下载库文件  下载地址： http://www.rarlab.com/rar/UnRARDLL.exe 

    2. 安装路径

    执行   UnRARDLL.exe  文件 ，路径选择默认 ，一般是C:\Program Files (x86)\UnrarDLL\ 目录下

    可以指到x64下。

    3. 添加系统环境变量

    在电脑 高级系统设置中，添加环境变量 变量名输入 UNRAR_LIB_PATH ，必须一模一样，变量值要特别注意！如果你是64位系统，就输入 C:\Program Files (x86)\UnrarDLL\x64\UnRAR64.dll，如果是32位系统就输入 C:\Program Files (x86)\UnrarDLL\UnRAR.dll 

    我多了一层x64目录，是最开始没找到64的dll文件，后面懒得改了。一般情况只有一层x64

    4. 最后需要重启IDE

"""
