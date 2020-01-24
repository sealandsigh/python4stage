# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/23

class Cat(object):
    """猫科动物类"""
    # 类的属性
    tag = "Cat base"

    def __init__(self,name):
        # 实例化后的属性
        self.name = name
        pass

    def eat(self):
        pass

class Tiger(Cat):
    pass