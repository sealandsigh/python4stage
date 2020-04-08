# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/8

from mongo_db import client
from gridfs import GridFS
from bson.objectid import ObjectId

db = client.school
gfs = GridFS(db,collection="book")
gfs.delete(ObjectId("5e8c94dbd2f8ad2bc2cc7403"))
