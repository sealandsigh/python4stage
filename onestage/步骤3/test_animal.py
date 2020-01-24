# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/23

class BaseCat(object):
    """
    猫科动物的基础类
    """
    tag = "猫科动物"

    def __init__(self,name):
        self.name = name

    def eat(self):
        print("猫吃东西")

class Tiger(BaseCat):
    # 调用父类的方法
    def eat(self):
        super(Tiger, self).eat()
        print("我还喜欢吃肉，大猪肉")


class Panda(BaseCat):
    pass


class PetCat(BaseCat):
    def eat(self):
        super(PetCat, self).eat()
        print("我还喜欢猫粮，大猪肉")


class HuaCat(PetCat):
    def eat(self):
        super(HuaCat, self).eat()
        print("我还喜欢零食，大猪肉")


class DuanCat(PetCat):
    pass


if __name__ == "__main__":
    cat = HuaCat("小黄")
    cat.eat()
    # 实例化英国短毛猫
    # 子类的判断
    print(issubclass(HuaCat,PetCat))