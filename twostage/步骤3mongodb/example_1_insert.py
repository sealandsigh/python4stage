# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/7

from mongo_db import client

client.school.teacher.insert_one({"name":"李璐"})
client.school.teacher.insert_many([
    {"name":"陈刚"},
    {"name":"郭丽丽"}
])