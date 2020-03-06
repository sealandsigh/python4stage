# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/6
from multiprocessing import Process,Queue, current_process

import time
import random


class WriteProcess(Process):
    """写的进程"""

    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        """实现进程的业务逻辑"""
        # 要写的内容
        ls = [
            "第一行内容",
            "第2行内容",
            "第3行内容",
            "第4行内容",
        ]
        for line in ls:
            print("写入内容 {0}-{1}".format(line,current_process().name))
            self.q.put(line)
            # 每写入一次，休息1-5秒
            time.sleep(random.randint(1,5))


class ReadProcess(Process):
    """读取的进程"""

    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            content = self.q.get()
            print("读取到的内容 {0}-{1}".format(content,current_process().name))


if __name__ == "__main__":
    q = Queue()
    t_write = WriteProcess(q)
    t_write.start()
    # 读取进程启动
    t_read = ReadProcess(q)
    t_read.start()
    t_write.join()

    # 因为读的进程是死循环，无法等待期结束，只能强制终止
    t_read.terminate()
