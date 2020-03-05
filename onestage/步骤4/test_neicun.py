# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/5

def extend_list(value,l=[]):
    print("--------------------------")
    print(l,id(l))
    l.append(value)
    print(l, id(l))
    return l

list1 = extend_list(10)
list2 = extend_list(123,[])
list3 = extend_list("a")

print(list1)
print(list2)
print(list3)

