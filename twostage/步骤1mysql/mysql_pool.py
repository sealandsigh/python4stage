# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/17

import mysql.connector
from mysql.connector import pooling

config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "zhujiajun",
    "database": "demo"
}


try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size = 10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = "UPDATE t_emp SET sal=sal+%s WHERE deptno=%s"
    cursor.execute(sql,(200,20))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)