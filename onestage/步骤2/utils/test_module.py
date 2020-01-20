# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/15
from datetime import datetime
from work.tools import get_file_type

from trans.tools import gen_trans_id

def test_trans_tool():
    """测试trans包下的tools模块"""
    id1 = gen_trans_id()
    print(id1)
    date = datetime(2015, 10, 2, 12, 30, 45)
    id2 = gen_trans_id(date)
    print(id2)

def test_work_tool():
    """测试work模块"""
    get_file_type()

if __name__ == "__main__":
    test_trans_tool()
    test_work_tool()