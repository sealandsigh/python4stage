# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/3

a = ['zhujiajun','jiaxuefeng','huangmengxi','nidaye']
a[0] = 'nihao'
print(a)

a[0:2] = ['nihao1','nihao2']
print(a)

a.remove('nihao1')
print(a)

a.pop(0)
print(a)
