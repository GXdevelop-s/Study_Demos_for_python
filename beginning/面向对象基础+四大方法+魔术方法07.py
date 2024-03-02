# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月27日
"""
import sys

# 类格式
'''
所有类名要求大写，多个单词用驼峰
class 类名 [(父类)]:
    属性:
    方法:

'''


class Phone:  # python可以给个空壳，从外部构建
    name = 'chushizhi'


nuojiya = Phone()  # 使用类构建对象
nuojiya.name = 'nuojiya'  # 改自己的属性
nuojiya.age = 6  # 直接给自己加属性，只是给自己加，不关同类对象的事情
Phone.name = 'change_default_value'  # 改类属性初始值


# 类中方法
# 种类： 普通方法 类方法 静态方法 魔术方法
class Phone2:
    # 类属性，可以通过类名直接调用
    electrity = True

    # 魔术方法之一：称作魔术方法__名字__()
    # 初始化，只要创建对象，如果有，系统默认执行
    def __init__(self, price, type):  # 发生在将内存地址赋值对象之前
        # 这些都是对象的属性，不是类的属性
        self.price = price
        self.type = type

    # 普通方法
    def call(self, logo):  # 这个self是当前对象，相当于java里面的this（调用的时候不用自己传递参数）
        print("calling")
        print('using huawei{}'.format(logo))  # 可以运行，但不能确保每一个对象都有这个成员的存在
        self.answer()  # 兄弟方法的调用，依然依赖于self

    def answer(self):
        print('i\'m listening')

    # 类方法 （不依赖于self对象的方法）
    # 不用创建对象，可以通过类名直接调用
    # 能访问类属性
    # 因为只能访问类的方法属性，所以可以在对象创建之前，完成一些动作
    # 类方法的第一个参数总是 cls。如果方法需要类的信息，用 @classmethod 对其进行装饰
    @classmethod
    def test(cls):  # cls class 是指当前类，不是一个对象
        print(cls)
        print(cls.electrity)

    # 静态方法
    # 静态方法也依赖于类，只能访问类的东西,
    # 无需传递参数,静态方法并不是真正意义上的类方法，它只是一个被放到类里的函数而已
    # 加载时机同类方法,静态方法通常用于组织代码，例如如果认为将某个函数放到某个类里，整体代码会因此更符合逻辑，于是可以将这个函数变成该类的静态方法。
    # 所以如果需要在类里放一个函数进去，此函数不会用到任何关于类或实例的信息，那么就可以用 @staticmethod 对其进行装饰。
    @staticmethod
    def silence():
        print(Phone2.electrity)


# 魔术方法01
# 普通方法需要调用，而魔术方法是在特定时刻自动触发
'''
__init__():初始化魔术方法
触发时机:初始化对象时触发

__new__():实例化的魔术方法 
触发时机:在实例化时触发
    new申请内存
    init初始化对象

__call__(): 调用对象的魔术方法
触发时机：将对象当作函数调用时触发 对象（）

__del__(): 析构魔术方法
触发时机：空间没有了引用，要被回收了
一般不自己写

'''


class Person:

    # 拿到new传过来的地址再扔给对象
    def __init__(self):
        print('--------->init')

    def __new__(cls, *args, **kwargs):
        print('--------->new')
        position = object.__new__(cls)  # 开辟空间,返回地址
        print(position)
        return position  # 开辟的地址扔出去给init

    # 把对象看作函数调用时本质调用的东西
    def __call__(self, *args, **kwargs):
        print('魔术方法call')

    # 当一块空间没有了引用，就会默认执行__del__; 或者程序结束时调用
    # 为了防止回收不到，知道就行，别写
    def __del__(self):
        print('------ 执行__del__')


p = Person()
p()  # 魔术方法call，想这么用就必须要重写
p1 = p
p2 = p1
print(sys.getrefcount(p))
del p1
print(sys.getrefcount(p))
del p2
print(sys.getrefcount(p))
del p  # 此时执行__del__
print(sys.getrefcount(p))

# 魔术方法02
'''
__str__(self): 
触发时机:打印对象名，自动触发调用
注意: 一定要再__str__方法中添加return
'''


class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


c1 = Cat('lsy')
print(c1)  # 单纯打印对象名称，出来的时一个地址，对于开发者来说无意义
