# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月30日
"""
# 私有化
'''
属性名前加__就代表私有化，外界拿不到，底层原理是伪装成另外的名字了
通过dir()函数可以找到这个名字，在拿到，但不建议这么用
需要set 和get函数提供获取和更改的方法
'''


# 初级
class Person:
    def __init__(self):
        self.__name = 'xu'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 4:
            print('false')
        else:
            self.__name = name


p1 = Person()
# print(p1.__name)  # 这里是无法获取到的
p1.set_name('gaoxu')
p1.get_name()  # set和get都是没有问题的，但要使用必须这样调函数


# 通过装饰器property实现的私有化（开发中常用）
# 高级
class Pig:
    def __init__(self):
        self.__name = 'yan'

    # 先有get的方法
    @property
    def name(self):
        return self.__name

    # 系统规定好了只要取值就去上面，赋值就去下面，函数名必须一样(且必须和变量名一样)
    # 才有set的方法，因为set依赖于get
    @name.setter
    def name(self, name):
        if len(name) > 4:
            print('false')
        else:
            self.__name = name


# 调用的方法和以前一样了，但是底层不一样了
lsy = Pig()
lsy.name = 'sy'  # 现在调用就成功了
print(lsy.name)

