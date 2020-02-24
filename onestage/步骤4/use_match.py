# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/24

import re

# 将正则表达式编译
pattern = re.compile(r'hello',re.I)
print(dir(pattern))

# 通过match来进行匹配
rest = pattern.match("Hello world!")
print(rest)

all_rest = re.match(r"hello","Hello world!",re.I)
print(all_rest)