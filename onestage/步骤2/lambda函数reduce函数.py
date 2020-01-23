# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/21

from functools import reduce

def get_sum(l):
    rest = 0
    for i in l:
        rest += i
    return rest

def f(m,n):
    return m + n

def get_sum_use_reduce(l):
    return reduce(f,l)

def get_sum_use_lambda(l):
    return reduce(lambda m,n: m + n ,l)

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9]
    rest = get_sum(l)
    print(rest)
    print("=======================")
    rest_reduce = get_sum_use_reduce(l)
    print(rest_reduce)
    print("=======================")
    rest_lambda = get_sum_use_lambda(l)
    print(rest_lambda)