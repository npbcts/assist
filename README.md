# assist
assist库是一个python模块,提供文件存储等多程序共用的服务脚本.
可以使用git的子模块工具部署在你git管理的项目中.

## 模块介绍

1. iocsv: 使用pandas库读取写入csv文件, 包含save_dict_csv, read_csv

2. iojson: 使用json库读取写入json文件,save_json, read_json

3. iopickle: 使用pickle库读取写入pickle文件,save_pickle, read_pickle

4. iotext: 读取写入text文件,save_text, read_text

5. mfolder: 针对文件夹的系列操作
- mk_folder: 创建文件夹
- rm_folder: 删除文件夹, 无论文件夹中是否有文件
- files_2_folder: 将某一文件夹中的指定多个(或一个)文件拷贝至另一个文件夹
- del_folder_files: 删除某一文件夹中的指定多个(或一个)文件

6. time_func: time_func: 测算程序运行时间的装饰器

7. zipfiles: 使用zipfile包形成系列文件的压缩包

