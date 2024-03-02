# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年09月25日
"""


import random

def get_minandmax(a):
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
    return a[0], a[len(a) - 1]


a = []
for i in range(0, 10):
    a.append(random.randint(1, 10))
b = get_minandmax(a)
print(b[0],b[1])
print("最大值是{0}最小值是{1}".format(b[0], b[1]))
