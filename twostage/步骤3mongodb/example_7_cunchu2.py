# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/8

from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId
import math
import datetime

db = client.school
gfs = GridFS(db,collection="book")
book = gfs.find_one({"filename":"7月汉堡王发票.pdf"})
print(book.filename)
print(book.type)
print(book.keyword)
print("{0}M".format(math.ceil(book.length/1024/1024)))
print("---------------------------------")
books = gfs.find({"type":"pdf"})
for one in books:
    uploadDate = one.uploadDate + datetime.timedelta(hours=8)
    uploadDate = uploadDate.strftime("%Y-%m-%d %H:%M:%S")
    print(one._id,one.filename,uploadDate)
print("=================================")
rs = gfs.exists(ObjectId("5e8c94dbd2f8ad2bc2cc7403"))
print(rs)
rs = gfs.exists(**{"type":"pdf"})
print(rs)
