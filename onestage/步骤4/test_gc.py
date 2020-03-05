# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/5

class Cat(object):

    def __init__(self):
        print("对象产生了,{0}".format(id(self)))

    def __del__(self):
        print("对象删除了,{0}".format(id(self)))


def f0():
    while True:
        c1 = Cat()


def f1():
    """这段代码会引起内存和cpu的无限增长"""
    l = []
    while True:
        c2 = Cat()
        l.append(c2)
        print(len(l))

if __name__ == "__main__":
    f0()

