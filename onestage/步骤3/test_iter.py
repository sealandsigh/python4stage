# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/16

class PowNumber(object):
    """迭代器
    生成 1，2，3，4，5   数的平方"""
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value * self.value

    def __iter__(self):
        return self

if __name__ == "__main__":
    pow = PowNumber()
    print(pow.__next__())
    print(pow.__next__())
    print(pow.__next__())
    print(next(pow))
    for i in pow:
        print(i)

