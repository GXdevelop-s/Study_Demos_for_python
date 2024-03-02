# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月11日
"""
import gevent
from gevent import monkey
monkey.patch_all()
import requests




def download(url):
    response = requests.get(url)
    print('受到来自{}的数据，数据长度：{}'.format(url, len(response.text)))


if __name__ == '__main__':
    targets = ['www.baidu.com', 'www.163,com', 'www.qq.com']
    g0 = gevent.spawn(download, targets[0])
    # g1 = gevent.spawn(download, targets[1])
    # g2 = gevent.spawn(download, targets[2])
    # gevent.joinall((g0, g1, g2))  # 一起阻塞
    g0.join()
    print('end')
