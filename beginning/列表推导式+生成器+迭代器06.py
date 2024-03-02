# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月25日
"""
# 列表推导式 字典推导式 集合推导式
# 旧的-->新的

# 1.列表推导式： 格式：[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]


names = ['tome', 'lily', 'sc', 'sss', 'dasjhd']
# 过滤掉长度等于或者小于3的名字
result = [name for name in names if len(name) >= 3]
# 首字母大写
result1 = [name.capitalize() for name in names if len(name) >= 3]
# 将1-100之间的数字能被3和5整除，组成一个新的列表
result2 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
# 使得10以内的所有奇偶组合组成一个元组列表
result3 = [(x, y) for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 != 0]  # 嵌套了一层for
# 直接推导的,取出3，6，9
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result4 = [i[-1] for i in list]
# 既有if又有else的情况
'''
else也有的情况下，整个ifelse结构就要写在前面了
若条件成立就要执行if前面的语句，若条件不成立就要执行else后面的语句
'''
dict1 = {'name': 'tom', 'salary': 4000}
dict2 = {'name': 'jery', 'salary': 5000}
dict3 = {'name': 'guard', 'salary': 2000}
list1 = [dict1, dict2, dict3]
result5 = [employee['salary'] + 200 if employee['salary'] >= 5000 else employee['salary'] + 1000 for employee in list1]

# 2.集合推导式{} 类型列表推导式，在列表推导式的基础上加了去除重复元素的作用
superfluous_list = [1, 21, 34, 4, 3, 41, 1, 4, 3, 1]
set = {x - 10 for x in superfluous_list if x > 30}

# 字典推导式
# 交换字典中key和value的值
dict = {'a': 'A', 'b': 'B', 'c': 'C', 'D': 'd'}
newdict = {value: key for key, value in dict.items()}

# 生成器
'''
通过列表推导式，可以直接创建列表
但是受到内存的限制，列表容量是有限的
而且，创建很大的空间如果访问不多，则会造成很大的到浪费
所以如果列表的元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后面的元素
这样不创建完整的list，从而节省空间，在python中，这种一边循环一边计算的机制，叫生成器：generator
'''
# 得到生成器的方式
'''
1.通过列表推导式得到生成器
把列表推导式的中括号改为小括号返回的就是一个生成器
'''
list2 = [x * 2 for x in range(20)]
print(type(list2))
# 得到生成器
g = (x * 3 for x in range(20))
print(type(g))
# 方法1：通过调用__next__()方式得到下一个元素
print(g.__next__())  # 0
print(g.__next__())  # 3
print(g.__next__())  # 6
# 方式2：使用系统自带的next函数，参数是生成器
print(next(g))  # 9
print(next(g))  # 12
print(next(g))  # 15
# StopIteration 超过本来产生的的元素就会抛出异常


'''
2.通过函数得到生成器
只要函数中出现了yield，说明函数就不是函数了，变成生成器了
步骤：
    定义一个函数，函数中是由yield关键字
    调用函数，接收调用的结果，结果就是生成器
'''


def func(len):
    n = 0
    while n < len:
        n += 1
        # print()
        yield n  # 相当于 return n +暂停
    return '报错信息'  # 当已经不符合要求时，返回值会返回return中的值，所以一般是提示报错信息


g = func(8)
print(next(g))
print(next(g))
print(next(g))

'''
生成器的方法：__next__()
send()      给生成器里面传数据的方法，第一次必须传None
以斐波那契数列举例
'''


def fib(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        tempt = yield b
        print('sand了{}'.format(tempt))
        a, b = b, a + b
        i += 1
    return '结束了'


g1 = fib(8)
g1.send(None)
g1.send(6)

# 生成器之多任务应用
'''
进程>线程>协程
通过多协程实现交替-- 即协程之间的通信！！
'''


def task1(n):
    for i in range(n):
        print('正在第{}次执行协程1'.format(i))
        yield None  # 协程切换


def task2(n):
    for i in range(n):
        print('正在第{}次执行协程2'.format(i))
        yield None


g1 = task1(5)
g2 = task2(5)
while True:
    try:
        g1.__next__()
        g2.__next__()

    except:
        break

# 迭代器
'''
迭代器是访问集合元素的一种方式 迭代器是一个可以记住遍历位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素 被访问完结束
迭代器只能往前不会后退
可以被next函数调用并不断返回下一个值的对象称为迭代器

但是可迭代的不一定是迭代器 比如 list就不是迭代器，但可以通过iter（）函数变成迭代器
'''
# 判断是否可迭代
from collections import Iterator

list3 = [1, 2, 3, 4]
bool1 = isinstance(list3, Iterator)  # 返回值类型布尔值
list3 = iter(list3)
a = Iterator()
a.__iter__()
bool2 = isinstance(list3, Iterator)
# 对一个对象调用iter（）方法会得到它的迭代器
'''
迭代器就是重复地做一些事情，可以简单的理解为循环，在python中实现了__iter__方法的对象是可迭代的，实现了next()方法的对象是迭代器，这样说起来有点拗口，
实际上要想让一个迭代器工作，至少要实现__iter__方法和next方法。
很多时候使用迭代器完成的工作使用列表也可以完成，但是如果有很多值列表就会占用太多的内存，而且使用迭代器也让我们的程序更加通用、优雅、pythonic。
'''


# 我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)    # 就会得到一个斐波那契数列
