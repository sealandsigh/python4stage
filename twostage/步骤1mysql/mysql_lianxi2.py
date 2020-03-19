# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/18

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
        pool_size=10
    )
    con = pool.get_connection()
    con.start_transaction()
    cursor = con.cursor()
    sql = "INSERT INTO t_dept" \
            "(SELECT MAX(deptno)+10,%s,%s FROM t_dept UNION " \
            "SELECT MAX(deptno)+20,%s,%s FROM t_dept )"
    cursor.execute(sql,("A部门","北京","B部门","上海"))
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)