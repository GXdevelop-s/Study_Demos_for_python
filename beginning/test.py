# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2023年01月01日
"""
class A:
    @staticmethod
    def test_a():
        print('I AM A')


class B(A):
    @staticmethod
    def test_b():
        print('I AM B')


class C(A):
    @staticmethod
    def test_c():
        print('I AM C')


class D(B, C):
    @staticmethod
    def test_c():
        print('I AM D')


class E(B, C):
    @staticmethod
    # def test_c():
    #     print('I AM E')

class F(D, E):
    @staticmethod
    def test_c():
        print('I AM F')


# 这个函数可以查看调用顺序
print(E.__mro__)  # 类名.__mro__
E.test_c()
