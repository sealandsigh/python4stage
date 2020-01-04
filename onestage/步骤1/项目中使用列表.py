# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/3

str = '张三,30,2000'
l = str.split(',')
print(l)
emp_list = []

while True:
    info = input('输入员工信息:' )
    if info == "":
        break
    info_list = info.split(',')
    print(info_list)
    emp_list.append(info_list)

print(emp_list)
print(emp_list)
print(emp_list)

