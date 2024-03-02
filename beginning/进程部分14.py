# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月03日
"""
import time
from multiprocessing import Process, Pool  # Process是一个类

import os
from random import random
from multiprocessing import Queue

# 进程创建
'''
Process(target=函数,name=进程的名字,args=(给函数传递的参数))
对象调用方法：
    process.start() 启动进程并执行任务
    process.run() 执行了任务但并没有启动程序
    terminate（）  终止进程
多进程对于全局变量访问，在每一个全局变量里面都放一个m变量
保证每个进程访问变量互不干扰（和可变不可变类型的变量没有关系）
'''

def task1(s):
    while True:
        time.sleep(s)
        # 得到进程号，和父进程号
        print('任务一执行中---{}-------{}\n'.format(os.getpid(), os.getppid()))


def task2(s):
    while True:
        time.sleep(s)

        print('任务二执行中---{}-------{}\n'.format(os.getpid(), os.getppid()))


num = 1
if __name__ == '__main__':
    p1 = Process(target=task1, name='任务1', args=(2,))  # 给进程起名任务1,把args传到task1中，（1，）是因为这个参数是要可迭代的（都行）
    p1.start()  # p.run() 只是让它去做这个动作，并不是正直的进程
    p2 = Process(target=task2, name='任务1', args=(2,))
    p2.start()
    print('---' * 5)  # 一般最先打印的是这个，但如果主进程时间片到了还没有打印，其他进程就会执行
    while True:
        num += 1
        time.sleep(0.2)
        if num == 100:
            p1.terminate()
            p2.terminate()
            break
        else:
            print(num)


# 自定义进程
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    # 重写run方法,run都要重写
    def run(self):
        print('------>自定义进程')
        print('进程名字' + self.name)


# 进程池（实现了进程的复用）
'''
当需要船舰的子进程不多时，可以直接利用multiprocessing中Process动态生成多个进程
但如果目标过多，手动的去创建工作量巨大，此时就可以利用到multiprocessing模块提供的Pool方法
初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool时，如果池还没有满
那么就会创建一个新的进程用来执行该请求：但如果池中的进程数已经达到指定的最大值，那么该请求就会等待
直到池中有进程结束，才会创建新的进程来执行

非阻塞式：
全部添加到队列中，立刻返回，并没有等待其他的任务执行完毕才结束，但是回调函数是等待任务完成之后才调用
进程池中会根据数量创建进程，假如任务数量大于池中最大进程数，那么第一个结束的进程会被下一个进来的进程使用（体现在进程号一样）
阻塞式：
也可以实现进程的复用，只不过，一个进程结束了，下一个进程才可以进来，底层没有队列了
'''


# 非阻塞式进程
def func(task_name):
    print('开始', task_name)
    print(1)
    start = time.time()
    time.sleep(random() * 5)
    end = time.time()
    print(start)
    print('任务完成{}用时：{} 进程id：{}'.format(task_name, end - start, os.getpid()))
    return
    #  return '任务完成{}用时：{} 进程id：{}'.format(task_name, end - start, os.getpid())  # 结果扔给了回调函数


# 回调函数就是任务执行完要调用的函数，必须加参数
def callback_func(n):
    print(n)


if __name__ == '__main__':
    func('TRY')
    print(time.time())
    pool = Pool(2)  # 得到进程池对象
    tasks = ['听音乐', '吃饭', '打游戏', '做饭', '睡觉', '散步']
    for task in tasks:
        # 非阻塞式，异步版本的apply，apply：equivalent to func()
        pool.apply_async(func, args=(task,))

    pool.close()  # 添加任务结束
    # 进程池不像子进程，不用管主进程，自己执行自己的；而是依赖于主进程，同生共死
    # 所以，要阻止主进程结束
    pool.join()  # 插队，阻挡主任务结束
    print('over!!')
# 阻塞式进程
    pool1 = Pool(2)  # 得到进程池对象
    tasks = ['听音乐', '吃饭', '打游戏', '做饭', '耍流氓', '散步']
    for task in tasks:
        # 非阻塞式，异步版本的apply，apply：equivalent to func()
        pool.apply(func, args=(task,))

    pool.close()  # 添加任务结束
    # 进程池不像子进程，不用管主进程，自己执行自己的；而是依赖于主进程，同生共死
    # 所以，要阻止主进程结束
    pool.join()  # 插队，阻挡主任务结束
    print('over!!')


# 进程间通信
'''
就是通过Queue作为桥梁和join控制执行顺序配合实现进程见通信
Queue还有：q.put_nowait和q.get_nowait （自学）
下文只讲Queue用法，通信详见demo9
'''
q = Queue(5)  # 创建一个队列，大小为5
q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')
print(q.qsize())  # 队列中装了几个
# 如果queue满了则只能等待，除非有空的
if not q.full():  # 判断队列是否满
    q.put('f', block=True, timeout=3)  # 阻塞？=True，等待时间三秒
else:
    print('队列已满')
# 获取队列的值
while True:
    print(q.get(timeout=1))

