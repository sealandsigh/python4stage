# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/21

def pow_number(l):
    rest_list = []
    for x in l:
        rest_list.append(x * x * x)
        return rest_list

# def f(n):
#     return n * n * n
#
# def pow_num_use_map(l):
#     return map(f,l)
#
# def pow_num_use_lambda(l):
#     return map(lambda n: n * n * n,l)

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,9]
    rest = pow_number(l)
    print(rest)