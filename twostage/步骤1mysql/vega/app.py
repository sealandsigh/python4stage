# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/19

from colorama import Fore,Style
from getpass import getpass
from service.user_service import UserService
import os

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
        if result == True:
            role = __user_service.search_user_role(username)
            os.system("clear")