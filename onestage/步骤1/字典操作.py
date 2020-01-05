# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/5

zhu_dict = {'name':'zhujiajun','age':23,'sex':'男'}

print(zhu_dict)

example_str = "姓名:{name},年龄:{age},性别:{sex}".format_map(zhu_dict)

print(example_str)