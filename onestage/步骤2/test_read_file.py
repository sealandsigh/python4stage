# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/23

f = open('test.txt')
# rest = f.read(8)
# print(rest)
# print(f.read(8))
#
# rest = f .readline()
# print(rest)
rest = f.readlines()
for i in rest:
    print(i)


f.close()
