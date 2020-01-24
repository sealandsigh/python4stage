# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/23


class Cat(object):
    """猫科动物类"""

    tag = "我是家猫"

    def __init__(self,name,age,sex=None):
        self.name = name
        self.__age = age
        self.sex = sex

    def set_age(self,age):
        """
        改变猫的年龄
        :param age: int 年龄
        :return: 更改后的年龄
        """
        self.__age = age
        return  self.__age

    def show_info(self):
        """显示猫的信息"""
        rest = "我叫{0},今年{1}岁".format(self.name,self.__age)
        print("我的性别是{0}".format(self.sex))
        print(rest)
        return rest

    def eat(self):
        """吃"""
        print("猫喜欢吃鱼")

    def catch(self):
        """猫捉老鼠"""
        print("猫捉老鼠")


if __name__ == "__main__":
    cat_black = Cat("小黑",2,"公的")
    cat_black.show_info()
    print("======================")
    print(cat_black.name)
    # print(cat_black.age)
    # print(cat_black.__age)
    cat_black.name = "heihei"
    cat_black.show_info()

    print("=======================")
    cat_black.set_age(7)
    cat_black.show_info()
    print(cat_black.tag)
    print(Cat.tag)

    #实例化小白
    cat_white = Cat('小白',3,"母的")
    print(cat_white.name)
    cat_white.show_info()
    print(cat_white.tag)

    # 类的实例判断
    print(isinstance(cat_black,Cat))
    print(isinstance(cat_white,Cat))
    print(isinstance(cat_black,Tiger))
    print(isinstance(cat_white,Tiger))