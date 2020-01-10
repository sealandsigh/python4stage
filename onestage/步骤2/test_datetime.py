# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/9

import datetime

now_time = datetime.datetime.now()

print("now:{0}".format(datetime.datetime.now()))

# 当前日期
print("now day: {0}".format(now_time.date()))

# 当前时间
print("now day: {0}".format(now_time.time()))
print("now day: {0}".format(datetime.datetime.today()))
print("now day: {0}".format(now_time.year))
print("now day: {0}".format(now_time.month))
print("now day: {0}".format(now_time.day))
