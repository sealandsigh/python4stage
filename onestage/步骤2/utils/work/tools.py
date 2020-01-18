# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/17

import os

def get_file_type(file_name):
    """
    根据文件的名称来判断文件类型
    :param file_name: str 文件名称
    :return: int 文件类型
    0: 图片类型文件
    1：word文档
    2： excel文档
    3： ppt文档
    """
    path,ext = os.path.splitext(file_name)
    if ext in ('.png','.jpg','.gif','.bmp'):
        return 0
