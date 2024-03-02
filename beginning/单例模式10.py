# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年11月10日
"""
# 单例模式
'''
单例的实质是内存的优化
单例模式是一种不受语言限制的开发模式，还有工厂模式等等
单例模式是指保证一个类只产生一个对象，或者说让一个类产生的所有对象都指向同一个地址，
要这个对象来解决问题
所以： 我们要他用过重写__new__方法来实现这一操作
'''


class Singleton:
    # 私有化--------唯一的地址就在这里
    __instance = None
    stuff = 'show method'

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 将申请到的地址保存在instance之中
            cls.__instance = object.__new__(cls)
            return cls.__instance  # 把创建好的地址返回给init函数
        # 如果不是第一次，就直接将该地址传递给init函数即可
        return cls.__instance

    @staticmethod
    def show(n):
        print(Singleton.stuff, n)


s1 = Singleton()
s2 = Singleton()
s1.show(1)
s2.show(2)
# 虽然是两个对象完成的，但是却是一个地址优化了内存
