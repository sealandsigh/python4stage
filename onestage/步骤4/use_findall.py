# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/24

import re

# 找出以下字符串的数字

content = "one1two2thrEe33four444five5six698"

# 使用编译的对象
p = re.compile(r"[a-z]+",re.I)
rest = p.findall(content)
print(rest)

# 不编译
all_rest = re.findall(r"[a-z]+",content,re.I)
print(all_rest)