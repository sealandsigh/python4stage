# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/6

from multiprocessing import Process, Lock, RLock

import time, random


class WriteProcess(Process):
    """写入文件"""

    def __init__(self, file_name, num, lock, *args, **kwargs):
        self.file_name = file_name
        self.num = num
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        """写入文件的主要业务逻辑"""
        with self.lock:
            # # 添加锁
            # self.lock.acquire()
            for i in range(5):
                with open(self.file_name,"a+", encoding="utf-8") as f:
                    content = "现在是 {0}:{1} - {2} \n".format(
                        self.name,
                        self.pid,
                        self.num
                    )
                    f.write(content)
                    time.sleep(random.randint(1,5))
                    print(content)


if __name__ == "__main__":
    file_name = "test.txt"
    # 锁的对象
    lock = RLock()
    for x in range(5):
        p = WriteProcess(file_name, x, lock)
        p.start()