# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/6
import time

from multiprocessing import Process

import os


def do_sth(name):
    """进程要做的事情"""
    print("进程名称 {0}, pid: {1}".format(name, os.getpid()))
    time.sleep(150)
    print("进程要做的事情")


class MyProcess(Process):

    def __init__(self,name,*args,**kwargs):
        self.my_name = name
        super().__init__(*args,**kwargs)

    def run(self):
        print("MyProcess进程名称 {0}, pid: {1}".format(self.my_name, os.getpid()))
        time.sleep(150)
        print("MyProcess进程要做的事情")


if __name__ == "__main__":
    # p = Process(target=do_sth, args=("my process",))
    p = MyProcess("my process class")
    # 启动进程
    p.start()
    # 挂起进程
