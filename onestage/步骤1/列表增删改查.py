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

print(a.count('nidaye'))

a.extend(['nidaye1','nidaye2'])
print(a)
a.append(['nidaye1','nidaye2'])
print(a)

person1 = a
person2 = a.copy()

print(person1 is a)
print(person2 is a)

a.clear()

print(person1)
print(person2)
