# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/11

class Cat(object):

    tag = "猫科动物"

    def __init__(self,name):
        self.name = name

    @staticmethod
    def breath():
        """呼吸"""
        print("猫都需要呼吸")

    @classmethod
    def show_info(cls):
        """显示猫的信息"""
        print("类的属性：{0}, 实例的属性: {1}".format(cls.tag,cls.name))

if __name__ == "__main__":
    # 通过类进行调用
    Cat.breath()
    cat = Cat("小黑")
    # 通过类的实例进行调用
    cat.breath()
    cat.show_info()