# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月06日
"""
import os
from multiprocessing import Process, Queue
from time import time, sleep


def download(q):
    with open(r'F:\pythonfiles\other corresponding files/t2.txt', 'r') as stream:
        container = stream.readlines()
    i = 1
    for line in container:
        try:
            q.put(line, timeout=5)  # 为了防止p1一直join
            print('第{}次下载，成功；进程号：{}'.format(i, os.getpid()))
            i += 1
        except Exception as err:
            break


def get_files(q):
    with open(r'F:\pythonfiles\other corresponding files/t3.txt', 'w') as stream:
        i = 1
        while True:
            try:
                stream.writelines(q.get(timeout=5))
                print('第{}次写入，成功；进程号：{}'.format(i, os.getpid()))
                i += 1
            except Exception as err:
                break


if __name__ == '__main__':
    q = Queue(10)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=get_files, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print('over!')