# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/14

from datetime import datetime,date,time,timedelta

# 自定义日期和时间
d = datetime(2020,10,30,14,5)
print(d)
d2 = date(2019,3,23)
print(d2)
t = time(9,0)
print(t)

print("------------------------")
# 日期 时间 与 字符串之间的相互转换
ds = '2018-10-3'
ds1 = '2018-10-3 13:42:09'
ds_t = datetime.strptime(ds,'%Y-%m-%d')
ds_t1 = datetime.strptime(ds1,'%Y-%m-%d %H:%M:%S')
print(ds_t.year)
print(ds_t1)
print("=========================")
n = datetime.now()
print(n)
print(n.strftime('%Y/%m/%d %H:%M:%S'))

# datetime之间的加减操作
n = datetime.now()
n_next = n + timedelta(days=5,hours=24)
print(n_next)

# 时间的减法
d1 = datetime(2020, 1, 15)
d2 = datetime(2020, 1, 16)
rest = d2 - d1
print(rest)
