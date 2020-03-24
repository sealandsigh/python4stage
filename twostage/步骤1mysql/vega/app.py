# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/19

from colorama import Fore,Style
from getpass import getpass
from service.user_service import UserService
import os
import sys
import time

__user_service = UserService()

while True:
    # os.system("clear")
    print(Fore.LIGHTBLUE_EX,"\n\t==================")
    print(Fore.LIGHTBLUE_EX,"\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t==================")
    print(Fore.LIGHTGREEN_EX,"\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX,"\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号:")
    if opt == "1":
        username = input("\n\t用户名:")
        password = getpass("\n\t密码:")
        result = __user_service.login(username,password)
        # 登录成功
        if result == True:
            # 查询角色
            role = __user_service.search_user_role(username)
            os.system("clear")
            while True:
                if role == "新闻编辑":
                    print("test")
                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX,"\n\t1 新闻管理")
                    print(Fore.LIGHTGREEN_EX,"\n\t2 用户管理")
                    print(Fore.LIGHTRED_EX,"\n\tback 退出登录")
                    print(Fore.LIGHTRED_EX,"\n\texit 退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号:")
                    if opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
        else:
            print("\n\t 登录失败")
            time.sleep(3)
    elif opt == "2":
        sys.exit(0)