# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/15
from datetime import datetime


def gen_trans_id(date=None):
    """
    根据所传入的时间得到一个唯一的交易流水ID
    :param date: 日期
    :return: 交易流水ID字符串
    """

    # 如果没有传入时间，则使用系统当前的时间
    if date is None:
        date = datetime.now()

    # 怎样保证字符串唯一
    # 日期+时间+毫秒+随机数（6位随机数)）
    return date.strftime("%y%m%d%H%M%S%f")