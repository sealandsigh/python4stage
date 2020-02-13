# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/11

def login(func):

    def wrapper():
        print("start")
        func()
        print("end")
    return wrapper

@login
def hello():
    print("hello")

hello()


