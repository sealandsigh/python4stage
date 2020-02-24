# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/24

import re

content = "hello world!"

p = re.compile(r"world")
# 使用search
rest = p.search(content)
print(rest)

# 使用match
match_rest = p.match(content)
print(match_rest)

# match vs search

