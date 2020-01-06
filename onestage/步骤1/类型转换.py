# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/6

l1 = [1,2,3,4,5]
l2 = (6,7,8,9)
l3 = ["1","2","3"]
str1 = 'abcd'
str2 = 'abc,def,age'
r1 = range(1,4)

l2_new = list(l2)
str1_new = list(str1)
str2_new = list(str2)
r1_new = list(r1)

print(l2_new,str1_new,str2_new,r1_new)

l1_tuple = tuple(l1)
str1_tuple = tuple(str1)
str2_tuple = tuple(str2)
r1_tuple = tuple(r1_new)

print(l1_tuple,str1_tuple,str2_tuple,r1_tuple)

print(str(l3))
print(",".join(l3))

