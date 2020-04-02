# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/2

from redis_db import pool
import redis

con = redis.Redis(
    connection_pool=pool
)

try:
    con.lpush("dname","董事会","秘书处","财务部","技术部")
    con.lpop("dname")
    result = con.lrange("dname",0,-1)
    for one in result:
        print(one.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con