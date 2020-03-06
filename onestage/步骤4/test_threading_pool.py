# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/5
import time,threading
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.dummy import Pool


def run(n):
    """线程要做的事情"""
    time.sleep(2)
    print(threading.current_thread().name,n)


def main():
    """使用传统的方法来做任务"""
    t1 = time.time()
    for n in range(100):
        run(n)
    print(time.time() - t1)

def main_use_thread():
    """ 使用线程优化任务 """
    # 资源有限，跑10个线程
    t1 = time.time()
    ls = []
    for count in range(10):
        for i in range(10):
            t = threading.Thread(target=run, args=(i,))
            ls.append(t)
            t.start()

        for l in ls:
            l.join()

    print(time.time() - t1)


def main_use_pool():
    """使用线程池优化"""

    t1 = time.time()
    n_list = range(100)
    pool = Pool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join()
    print(time.time() - t1)


def main_use_executor():
    """使用 ThreadPoolExecutor 来优化"""
    t1 = time.time()
    n_list = range(100)
    with ThreadPoolExecutor(max_workers=10) as  executor:
        executor.map(run,n_list)
    print(time.time() - t1)



if __name__ == "__main__":
    # main_use_thread()
    # main_use_pool()
    main_use_executor()