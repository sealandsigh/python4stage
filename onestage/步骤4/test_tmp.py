# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/16

def del_item(lst,e):
    return [ lst.remove(i) for i in lst if i==e]

def del_item(lst,e):
    d = dict(zip(range(len(lst)),lst)) # YES! 构造字典
    return [v for k,v in d.items() if v!=e]


if __name__ == "__main__":
    l = ['a', 'b', 'c', 'd', 'e', 'f']
    a = l[:-1]
    b = l[1:]
    rest = zip(a,b)
    print(rest)
    print(zip(l[:-1], l[1:]))
    print(range(0,10))

