# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/8

from pymongo import MongoClient

client = MongoClient(host="10.10.129.90",port=27017)
client.admin.authenticate("admin","123456")