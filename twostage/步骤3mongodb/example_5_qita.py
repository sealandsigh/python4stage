# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/7

from mongo_db import client

students = client.school.student.find({}).skip(0).limit(10)
for one in students:
    print(one["_id"],one["name"])

names = client.school.student.distinct("name")
print(names)

students = client.school.student.find({}).sort([("name",-1)])
for one in students:
    print(one["_id"],one["name"])