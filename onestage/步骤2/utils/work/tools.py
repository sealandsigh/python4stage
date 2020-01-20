# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/17

import os

def get_file_type(file_name):
    """
    根据文件的名称来判断文件类型
    :param file_name: str 文件名称
    :return: int 文件类型
    -1： 未知文件类型
    0: 图片类型文件
    1：word文档
    2： excel文档
    3： ppt文档
    """
    # 默认文件是未知类型
    result = -1
    # 传进来的必须是一个文件的名称
    if not os.path.isfile(file_name):
        return result
    path,ext = os.path.splitext(file_name)
    ext = ext.lower()

    if ext in ('.png','.jpg','.gif','.bmp'):
        result = 0

    elif ext in ('.doc','.docx'):
        result = 1

    elif ext in ('.ppt','.pptx'):
        result = 2
    elif ext in ('.xls','.xlsx'):
        result = 3

    return result