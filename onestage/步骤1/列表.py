# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/3

i = 0
count = 0
a = ['zhujiajun','liudi','mengxi','zhujiajun']
print(a)

print(len(a))

for p in a:
    if p == 1:
        print('ok',i)
    i += 1

a.reverse()
print(a)

b = [28,32,14,15,22,54,42]

b.sort(reverse=True)
print(b)