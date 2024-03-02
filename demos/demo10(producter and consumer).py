# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月11日
"""
import random
import threading
import time
from threading import Thread
import queue

q = queue.Queue(maxsize=5)


def product(q):
    for i in range(5):
        data = str(random.randint(1, 1000))
        q.put('产品号：' + data)
        print('生产者第{}次生产{}'.format(i, data), end=' ')


def consumer(q):
    while True:
        data = q.get()
        print('取得产品，' + data)
        time.sleep(1)
        q.task_done()  # task_done只是一个标记，让队列未被处理元素数-1，如果队列未被处理元素数=0，就不阻塞
        print(q.empty())  # get 会取出，而不只是访问，所以取到最后，就会是True


if __name__ == '__main__':
    t1 = threading.Thread(target=product, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    q.join()  # 只要队列未被处理元素数小于等于0，立马释放，不阻塞了，但如果队列一开始就为空，而且生产者放的比较慢，就会直接释放

    print('end')
