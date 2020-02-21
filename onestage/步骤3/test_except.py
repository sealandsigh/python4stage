# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/21

import os
import os.path

def test_div(num1,num2):
    """当除数为0时候"""
    return num1 / num2

def test_file():
    file_path = os.path.abspath(__file__)
    base_path = os.path.dirname(file_path)
    real_file_path = os.path.join(base_path,"test_file.txt")
    try:
        f = open(real_file_path,"r")
        rest = f.read()
        print(rest)
    except:
        print("error")
    finally:
        f.close()
        print("closed")

if __name__ == "__main__":
    # try:
    #     rest = test_div(5,'s')
    #     print(rest)
    # except ZeroDivisionError:
    #     print("报错了，除数不能为0")
    # except TypeError:
    #     print("报错了，请输入数字")
    # try:
    #     rest = test_div(5,'s')
    #     print(rest)
    # except (ZeroDivisionError,TypeError) as e:
    #     print(e)
    test_file()