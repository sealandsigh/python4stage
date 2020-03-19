# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/19

import mysql.connector.pooling

__config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "zhujiajun",
    "database": "vega"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)