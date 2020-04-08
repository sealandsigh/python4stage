# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/8

from db.mongo_db import client
from bson.objectid import ObjectId

class MongoNewsDao(object):
    # 添加新闻正文记录
    def insert(self,title,content):
        try:
            client.vega.news.insert_one({"title":title,"content":content})
        except Exception as e:
            print(e)


    def search_id(self,title):
        try:
            news = client.vega.news.find_one({"title":title})
            return str(news["_id"])
        except Exception as e:
            print(e)

    def update(self,id,title,content):
        try:
            client.vega.news.update_one({"_id":ObjectId(id)},
                                        {"$set":{"title":title,"content":content}})
        except Exception as e:
            print(e)

    def search_content_by_id(self,id):
        try:
            news = client.vega.news.find_one({"_id":ObjectId(id)})
            return news["content"]
        except Exception as e:
            print(e)