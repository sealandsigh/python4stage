# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/23

class PetCat(object):
    """家猫类"""

    def __init__(self,name,age):
        """
        构造方法
        :param name: 猫的名称
        :param age: 猫的年龄
        """
        self.name = name
        self.age = age

    # 描述符
    @property
    def show_info(self):
        """显示猫的信息"""
        return "我叫{0}，今年{1}岁".format(self.name,self.age)

    def __str__(self):
        return "我的对象: {0}".format(self.name)


if __name__ == "__main__":
    cat_balck = PetCat("小黑",2)
    rest = cat_balck.show_info
    print(rest)
    # print(cat_balck)