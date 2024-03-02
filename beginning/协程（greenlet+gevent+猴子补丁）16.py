# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月11日
"""
# 协程：微线程（底层是生成器）
import time

import gevent
import greenlet
from gevent import monkey  # 大圣要单独叫

'''
协程：耗时操作
耗时操作：网络请求 网路下载（爬虫） IO:文件的读写 阻塞
生成器写法同之前，现在可直接用 greenlet模块（需下载）完成携程任务,使得切换任务比较简单（手动切换）
还有可以自动切换任务的模块 gevent
'''


# greenlet
def a():
    for i in range(4):
        print('A', i)
        gb.switch()  # 虽然不加sleep结果也是一样的，但是这就保证了睡了没关系
        time.sleep(0.5)


def b():
    for i in range(4):
        print('B', i)
        gc.switch()
        time.sleep(0.5)


def c():
    for i in range(4):
        print('C', i)
        ga.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    ga = greenlet.greenlet(a)
    gb = greenlet.greenlet(b)
    gc = greenlet.greenlet(c)
    # ga.switch()

# gevent
'''
当一个greenlet遇到IO（input和output、网络、文件操作），就会自动切换到其它的greenlet，等到IO完成
由于IO操作非常耗时。经常使程序输液 等待状态，有了gevent就可以自动切换协程
就保证总有greenlet在运行而不是在等待IO

'''
# 猴子补丁的monkey.patch_xxx()来将python标准库中模块或函数改成gevent中的响应的具有协程的协作式对象。这样在不改变原有代码的情况下，将应用的阻塞式方法，变成协程式的。
monkey.patch_time()  # 替换了time模块


def d():
    for i in range(4):
        print('A', i)
        time.sleep(0.5)


def e():
    for i in range(4):
        print('B', i)
        time.sleep(0.5)


def f():
    for i in range(4):
        print('C', i)
        time.sleep(0.5)


if __name__ == '__main__':
    #  Create a new :class:`Greenlet` object and schedule it to run ``function(*args, **kwargs)``.
    #  This can be used as ``gevent.spawn`` or ``Greenlet.spawn``.
    g1 = gevent.spawn(d)
    g2 = gevent.spawn(e)
    g3 = gevent.spawn(f)
    # 如果主进程结束gevent和greenlet就不工作了
    g1.join()
    g2.join()
    g3.join()
    print('--------')