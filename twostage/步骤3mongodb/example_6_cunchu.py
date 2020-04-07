# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/7

from mongo_db import client
from gridfs import GridFS

db = client.school
gfs = GridFS(db,collection="book")

file = open("/Users/jiajun.zhu/Downloads/7月汉堡王发票.pdf","rb")
args = {"type":"pdf","keyword":"linux"}
gfs.put(file,filename="7月汉堡王发票.pdf",**args)
file.close()
