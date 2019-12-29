# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2019/12/29


j = 2
while j < 1000:
    i = 2
    num = j
    while i < num:
        if num % i == 0:
            # print('{} is 不是质数'.format(num))
            i += 1
            continue
        else:
            print('{} is 质数'.format(num))
            break
    j += 1