# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/3

from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    con.hmset("9527",{"name":"Scott","sex":"male","age":35})
    con.hset("9527","city","纽约")
    con.hdel("9527","age")
    result = con.hexists("9527","name")
    print(result)
    result = con.hgetall("9527")
    for one in result:
        print(one.decode("utf-8"),result[one].decode("utf-8"))

except Exception as e:
    print(e)
finally:
    del con