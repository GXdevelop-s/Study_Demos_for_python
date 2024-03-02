# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月30日
"""
# 关联
'''
就是一个类用了另一个类
'''

# 继承
'''
格式

class 类名（父类）:
    
子类的init要调用父类的init才可以
用super（）调用父类init的self是指子类对象    
子类调用父类的init是有三种写法的
'''


class Person:
    def __init__(self, name):
        print('Person 的 __init__')
        print(name)

    @classmethod
    def eat(cls):  # 如果函数中没有用到这个类的属性，那么python会认为这应该是一个静态的方法
        print('Person 在吃')


class Stu(Person):
    def __init__(self, name, given):
        super().__init__(name)  # super（）父类对象
        self.secret_money = given

    @classmethod
    def eat(cls):
        print('Stu 在吃')


s1 = Stu('xu', 1)


class Doc(Person):
    def __init__(self, name, patient):
        super(Doc, self).__init__(name)  # 这种写法相当于底层多加了一层判断，isinstance self是不是Doc
        self.patient = patient

    @classmethod
    def eat(cls):
        print('Doc 在吃')


'''
继承特点：
    1.如果类中不定义init，调用父类的init
    2.如果继承父类也需要定义自己的init，就需要在当前类的init调用一下父类
    3.两种super方式
    4.函数和父类中函数名相同则遵循重写的原则
'''

# 关于重载
'''
如果在一个类中定义两个不同形参的同名函数，后面的会把前面的覆盖掉
也就是  不  支   持   重    载  ！  ！
'''

# 多继承
'''
python中支持多继承，一个类可以继承多个父类
def 子类（父类1，父类2...）:
    pass
python多继承搜索问题    
    从左至右，广度优先 （python3）
    经典类深度优先，新式类广度优先（python2）
    
'''


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
    def test_c():
        print('I AM E')


class F(D, E):
    @staticmethod
    def test_c():
        print('I AM F')


# 这个函数可以查看调用顺序
print(E.__mro__)  # 类名.__mro__

# 多态
'''
在python中没有严格的判断，形参可以接收各种类型，并不是只有该类和子类
但是接收参数之后要依赖isinstance（obj,类）来进行判断
判断的是 是否是该类和该类的子类
写一个例子
'''


class Pet:
    def __init__(self, name):
        self.name = name

    def shou(self, pet):
        if isinstance(pet, Pet):
            print(pet.name)


class Cat(Pet):
    name = 'cat'


class Tiger():
    name = 'tiger'


pet1 = Pet('a')
cat1 = Cat('b')
tiger1 = Tiger()
pet1.shou(cat1)  # 都可以接收，不严格多态
pet1.shou(tiger1)
