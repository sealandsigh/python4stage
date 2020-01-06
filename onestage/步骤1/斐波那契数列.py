# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/6

# 斐波那契数列
# 1，1，2，3，5,8,13

result = []
for i in range(0,50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i-2]+result[i-1])

print(result)