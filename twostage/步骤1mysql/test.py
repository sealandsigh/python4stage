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
# sql = "SELECT empno,ename,hiredate FROM t_emp;"
sql = "INSERT INTO t_emp(empno,ename,job,mgr,hiredate,sal,comm,deptno) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
# rest = cursor.execute(sql)
# for one in cursor:
#     print(one[0],one[1],one[2])
cursor.execute(sql,(9600,"赵娜","SALESMAN",None,"1985-12-1",2500,None,10))
con.commit()
con.close()
