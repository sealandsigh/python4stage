# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/21

def user_file(l):
    """
    lambda 练习
    :param l: 列表
    :return: 值
    """
    rest = filter(lambda n: n % 2 != 0,l)
    return rest

if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9]
    test = user_file(l)
    print(list(test))