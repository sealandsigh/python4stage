# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/11

def hello():
    """简单功能模拟"""
    print("hello work")

def test():
    print("test...")

def hello_wrapper():
    print("开始执行hello")
    hello()
    print("结束执行hello")

def test_wrapper():
    print("开始执行hello")
    test()
    print("结束执行hello")

if __name__ == "__main__":
    # hello()
    hello_wrapper()