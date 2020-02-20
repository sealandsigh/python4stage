# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/18

import os
import os.path

class FileBackup(object):
    """文本文件备份"""

    def __init__(self,src,dist):
        """
        构造方法
        :param src: 目录 需要备份文件的目录
        :param dist: 目录 备份后的目录
        """
        self.src = src
        self.dist = dist


    def read_files(self):
        """
        读取src目录下的所有文件
        :return:
        """
        ls = os.listdir(self.src)
        print(ls)
        for l in ls:
            self.backup_file(l)

    def backup_file(self,file_name):
        """
        处理备份
        :param file_name: 文件/文件夹的名称
        :return:
        """
        pass
        # 1 判断dist目录是否存在，如果不存在，要创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的目录不存在，创建完成")

        # 2 判断文件是否为要备份的

        # 拼接完整路径
        full_path = os.path.join(self.src,file_name)
        # 首先要判断是否为文件夹，然后可以借助于文件的后缀进行判断
        if os.path.isfile(full_path) and os.path.splitext(full_path)[-1].lower() == ".txt":
            print(full_path)
        # 3 读取文件内容
            with open(full_path,"r",encoding="utf-8") as f_src:
                rest = f_src
        # 4 读取的内容写入到新的文件当中
        else:
            print("文件类型不符合备份系统，跳过")


if __name__ == "__main__":
    # src_path = "/Users/jiajun.zhu/Documents/pythonproject/python4stage/onestage/步骤3/src"
    # dist_path = "/Users/jiajun.zhu/Documents/pythonproject/python4stage/onestage/步骤3/dist"
    base_path = os.path.dirname(os.path.abspath(__file__))
    print(base_path)
    src_path = os.path.join(base_path,"src")
    dist_path = os.path.join(base_path,"dist")
    print(src_path)
    print(dist_path)
    bak = FileBackup(src_path,dist_path)
    bak.read_files()
