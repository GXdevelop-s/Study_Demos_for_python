# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月07日
"""
# python多线程
import time

'''
python 通过两个标准库thread和threading提供对线程的支持
thread提供的低级别的、原始的线程以及一个简单的锁
所以我们用threading模块

线程的五个状态：新建，就绪，运行，阻塞，结束
线程是可以共享全局变量的（记得加global）
GIL 全局解释器锁
python底层只要用线程默认加锁————一个线程进来就上锁，不让其他线程进来，保证了数据安全，但是牺牲了效率
当cpu计算量变得比较大得时候，这把锁就会被自动释放
t.setDaemon(True)  设置守护线程，主程序结束后会强制结束该线程
'''
import threading
from time import sleep
import random

n = 0


def task(x):
    global n
    for i in range(10000000):  # 此时GIL锁被打开了
        n += 1
    print('{}:{}'.format(x, n))


def download(n):
    images = ['a.jpg', 'b.jpg', 'c.jpg', 'd.jpg']
    for image in images:
        print('正在下载{}'.format(image))
        sleep(n)
        print('下载{}成功'.format(image))


def delete(n):
    images = ['del_a.jpg', 'del_b.jpg', 'del_c.jpg', 'del_d.jpg']
    for image in images:
        print('正在{}'.format(image))
        sleep(n)
        print('{}成功'.format(image))


if __name__ == '__main__':
    t1 = threading.Thread(target=download, name='图片下载器', args=(1,))
    # t1.start()
    t2 = threading.Thread(target=delete, name='图片下载器', args=(1,))
    # t2.start()
    # 运行时，由于sleep会让出执行权，所以会出现两个线程交替输出的情况，如果去掉t1的sleep那么t1会一直执行到底
    t3 = threading.Thread(target=task, args=('增量线程1',))
    t4 = threading.Thread(target=task, args=('增量线程2',))
    t3.start()
    t4.start()
    t3.join()  # 必须加join，不然主程序会先打印
    t4.join()
    print(n)

# 线程与进程
'''
线程：耗时操作，爬虫 IO
进程：计算密集型
'''

# 多线程同步
'''
共享数据：
如果多个线程共同对某个数据修改，则可能出现不可预估的的结果，为了保证数据的正确性，需要对多个线程进行同步
同步：一个一个完成，一个做完另一个才能进来；效率就会降低
使用 Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire和release方法
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间

'''
lock = threading.Lock()
list1 = [0] * 10


def put_in():
    # 获取线程锁，如果已经上锁，则等待锁的释放
    lock.acquire()  # 请求锁，返回值是布尔类型
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()  # 释放锁


def get_out():
    # 获取线程锁，如果已经上锁，则等待锁的释放
    lock.acquire()  # 阻塞
    for i in range(len(list1)):
        print('---->', list1[i])
        time.sleep(0.5)
    lock.release()


if __name__ == '__main__':
    tp = threading.Thread(target=put_in)
    tg = threading.Thread(target=put_in)
    tp.start()
    tg.start()

# 下面写个死锁
'''
如何解决死锁：
1.重构
2.给acquire加timeout
'''
locka = threading.Lock()
lockb = threading.Lock()


class Mythread1(threading.Thread):
    def run(self):
        if locka.acquire() is True:
            print('{}已经拿到A锁'.format(self.name))
            sleep(0.5)
            if lockb.acquire() is True:
                print('{}已经拿到B锁，且拥有A锁'.format(self.name))
                lockb.release()
            locka.release()


class Mythread2(threading.Thread):
    def run(self):
        if lockb.acquire() is True:
            print('{}已经拿到B锁'.format(self.name))
            sleep(0.5)
            if locka.acquire() is True:
                print('{}已经拿到A锁，且拥有B锁'.format(self.name))
                lockb.release()
            locka.release()


if __name__ == '__main__':
    mt1 = Mythread1()
    mt2 = Mythread2()
    mt1.start()
    mt2.start()

# 生产者与消费者：两个线程之间的通信
'''
python的queue模块中提供了同步的、线程安全的队列类，包括
FIFO队列Queue
LIFO队列LifoQueue
优先级队列PriorityQueue
这些队列都实现了锁原理（原子操作）
能够在多线程中直接使用，来实现线程之间的同步
详见 demo10
'''