# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/16

def pow():
    yield 1
    yield 2
    yield 3
    yield 4

if __name__ == "__main__":
    rest = pow()
    print(rest)
    print(next(rest))
    print(next(rest))
    print(next(rest))
    print(next(rest))
    print(next(rest))

