# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/1/5

# 处理员工信息
source = "7782,clark,manage,sales,5000$7934,mtille,salesman,sales,3000$9981,test,deploy,sales,6000"
employee_list = source.split('$')
print(employee_list)

# 保存所有解析后的员工信息，key是员工编号，value则是包含完整员工信息的字典
all_emp = {}

for i in range(0,len(employee_list)):
    # print(i)
    e = employee_list[i].split(',')
    print(e)

    #创建员工字典
    employee = {"no":e[0],'name':e[1],'job':e[2],'department':e[3],'salery':e[4]}
    print(employee)
    print(employee)