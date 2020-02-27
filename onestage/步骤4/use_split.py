# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/2/26

import re

s = "one1two2three333four4five5six6"
p = re.compile(r"\d+")
rest = p.split(s,2)
print(rest)
