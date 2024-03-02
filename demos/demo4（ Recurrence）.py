# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月18日
"""


def fbnq(x):
    if x == 1 or x == 0:
        return 1
    else:
        return fbnq(x - 1) + fbnq(x - 2)


v = []
n = int(input('how many items do you want'))
for i in range((n)):
    v.append(fbnq(i))
for j in v:
    print(j)
