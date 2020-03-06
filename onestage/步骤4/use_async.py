# -*- coding: utf-8 -*-
# __author__="jiajun.zhu"
# DATE:2020/3/6

import asyncio

async def do_sth(x):
    """定义携程函数"""
    print("等待中: {0}".format(x))
    await asyncio.sleep(x)

# 判断是否为携程函数
print(asyncio.iscoroutinefunction(do_sth))

coroutine = do_sth(5)
# 事件循环队列
loop = asyncio.get_event_loop()
# 注册任务
task = loop.create_task(coroutine)
print(task)
# 等待携程任务执行结束
loop.run_until_complete(task)
print(task)



