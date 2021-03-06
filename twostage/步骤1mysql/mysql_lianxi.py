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
    # sql = "CREATE TABLE t_emp_new AS (SELECT * FROM t_emp)"
    sql = "DROP TABLE t_emp_new"
    cursor.execute(sql)
    sql = "CREATE TABLE t_emp_new LIKE t_emp"
    cursor.execute(sql)
    # 使用insert语句，把部门平均底薪超过公司平均底薪的部门里的员工信息放到t_emp_new里，并且让这些员工隶属于sales部门
    sql = "SELECT AVG(sal) AS avg FROM t_emp"
    cursor.execute(sql)
    temp = cursor.fetchone()
    avg=temp[0] # 公司的平均底薪
    sql = "SELECT deptno FROM t_emp GROUP BY deptno HAVING AVG(sal)>=%s"
    cursor.execute(sql,[avg])
    # for one in cursor:
    #     print(one[0])
    temp = cursor.fetchall()
    print(temp)
    sql = "INSERT INTO t_emp_new SELECT * FROM t_emp WHERE deptno IN ("
    for index in range(len(temp)):
        sql += str(temp[index][0])
        if index < len(temp) - 1:
            sql += ","
    sql += ")"
    cursor.execute(sql)
    sql = "DELETE FROM t_emp WHERE deptno IN ("
    for index in range(len(temp)):
        one = temp[index][0]
        if index < len(temp) - 1:
            sql += str(one) + ","
        else:
            sql += str(one)
    sql += ")"
    cursor.execute(sql)
    sql = "SELECT deptno FROM t_dept WHERE dname=%s"
    cursor.execute(sql,["SALES"])
    deptno = cursor.fetchone()[0]
    sql = "UPDATE t_emp_new SET deptno=%s "
    cursor.execute(sql,[deptno])
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)