# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月18日
"""
from functools import reduce


# 匿名函数实际开发应用场景------匿名函数作为参数来使用
def func1(a, f):  # f=lambda x:x**2
    print('a')
    r = f(a)
    print(r)


func1(8, lambda x: x ** 2)

# 函数高阶
# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，同样，我们还可以
# 把一个函数当作另一个函数的返回值。这样的使用方式为      函数高阶

# 系统高阶
list1 = [('a', 1), ('b', 4), ('c', 2), ('d', 10)]
m = max(list1, key=lambda x: x[1])  # 注意这里key是关键字了，不能随意取名字
print(m)

s = sorted(list1, key=lambda x: x[1], reverse=True)  # 以指定的方式进行排序
print(s)

f = filter(lambda x: x[1] >= 4, list1)  # 第一个参数必须是一个返回布尔类型的方法，或者是空；boolean值为真则返回过滤结果
print(f)  # filter 的返回值是一个filter对象
print(list(f))  # 这种的强转成list就可以看到结果了，但是提取的是原对象（元组）

# 通过function提取list1中符合条件的内容，并加工
ma = map(lambda x: x[0].title(), list1)  # map是函数映射
print(list(ma))  # 返回值是一个map对象，想提取哪个就提取哪个

# 进行压缩运算，并得到一个值，这个不是系统的函数;  这个函数被移到了 functools 模块
r2 = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 运算过程，第一次取两个数作为参数按照函数运算，结果和下一个数再作为x，y进行运算最后得到一个数
print(r2)
