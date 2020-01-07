# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/6

# 生成式
list1 = []
for i in range(10,20):
    list1.append(i*10)
print(list1)

list2 = [i * 10 for i in range(10,20)]
print(list2)

lst3 = [i* 10 for i in range(10,20) if i % 2 == 0]
print(lst3)

lst4 = ["zhangsan","lisi","wangwu"]

new_dict = { i+1:lst4[i] for i in range(0,len(lst4))}
print(new_dict)

# 集合生成式
set1 = {i*j for i in range(1,4) for j in range(1,4) if i == j}
print(set1)