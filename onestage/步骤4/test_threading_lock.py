# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/5

import threading,time

# 获得一把锁
my_lock = threading.Lock()
your_lock = threading.RLock()

# 我的银行账户
balance = 0


def change_it(n):
    """改变我的余额"""
    global balance

    # 方式1 选择with
    with your_lock:
        balance = balance + n
        time.sleep(2)
        balance = balance - n
        time.sleep(1)
        print("===N============ {0}; balance: {1}".format(n, balance))

    # 方式二
    # try:
    #     # 添加锁
    #     my_lock.acquire()
    #     balance = balance + n
    #     time.sleep(2)
    #     balance = balance - n
    #     time.sleep(1)
    #     print("===N============ {0}; balance: {1}".format(n,balance))
    # finally:
    #     # 释放锁
    #     my_lock.release()


class ChangeBalanceThread(threading.Thread):

    def __init__(self,num,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.num = num

    def run(self):
        for i in range(1000):
            change_it(self.num)


if __name__ == "__main__":
    t1 = ChangeBalanceThread(5)
    t2 = ChangeBalanceThread(8)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("the last {0}".format(balance))
