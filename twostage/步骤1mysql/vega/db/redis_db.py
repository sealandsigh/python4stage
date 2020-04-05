# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/4/1

import redis

try:
    pool = redis.ConnectionPool(
        host = "10.10.129.90",
        port = 6379,
        password = "zhujiajun",
        db = 1,
        max_connections = 20
    )
except Exception as e:
    print(e)
