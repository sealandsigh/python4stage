# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/17

import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",port="3306",
#     user="root",password="zhujiajun",
#     database="demo"
# )
#
# con.close()

config = {
    "host": "localhost",
    "port": "3306",
    "user": "root",
    "password": "zhujiajun",
    "database": "demo"
}

con = mysql.connector.connect(**config)
cursor = con.cursor()
sql = "SELECT empno,ename,hiredate FROM t_emp;"
rest = cursor.execute(sql)
for one in cursor:
    print(one[0],one[1],one[2])
con.close()
