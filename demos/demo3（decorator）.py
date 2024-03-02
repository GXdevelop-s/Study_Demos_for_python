# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月14日
"""


# 装饰器（夺舍）

def decorator(fun):
    def wrapper():
        fun()  # 这样就保证了原函数内部的代码不变
        print('添砖')
        print('加瓦')
        print('找女友')

    return wrapper


@decorator  # 就相当于是调用函数  ——get_a_house= decocrator(get_a_house)
def get_a_house():
    print('maopifang')


get_a_house()

# 实现过程
# 1.内存先加载decorator和get_a_house函数 并执行@decorator
# 2.执行decorator函数，此时参数就是get_a_house,传入的是该函数的地址，
# 3.返回值却是wrapper函数的地址，相当于，get_a_house函数指向了warpper函数，简单来说就是get_a_house函数的地址被换成了wrapper函数的地址
# 4.这时代码在第25行执行，实际上却执行的是wrapper函数了，实现了装饰作用
print('------------------------------')


# 有参数的装饰器
def decorator2(fun):
    def wrapper(*args, **kwargs):  # 要考虑到多参数和关键字参数的情况
        fun(*args, **kwargs)  # 这样就保证了原函数内部的代码不变
        print('添砖')
        print('加瓦')
        print('找女友')

    return wrapper


@decorator2
def get_a_motel(square, name='7tian', location='beijing'):
    print('there is a motal called {},and its square is{},located in {}'.format(name, square, location))


get_a_motel(66)

print('------------------------------')


# 带返回值的装饰器
def decorator3(fun):
    def wrapper(*args, **kwargs):
        r = fun(*args, **kwargs)
        print('添砖')
        print('加瓦')
        print('找女友')
        r = r * 2  # 对初始值进行修饰
        return r  # 这里返回才是函数外部调用的值

    return wrapper


@decorator3
def get_a_hotel():
    r = 5000
    return r  # 这里的返回是返回到闭包内层


aset = get_a_hotel()
print(aset)


# 带参数的装饰器
def outer_check(time):  # 执行输出1，加载check time，执行输出2，返回check time的地址
    print('-----------1')

    def check_time(action):  # 此时调用check_time就要起到装饰器的作用将play game作为参数传入了，返回的do_action变成了真正的play_game函数
        print('-----------3')

        def do_action():
            if time < 22:
                return action()
            else:
                return 'you are not mandated'

        print('-----------4')
        return do_action()

    print('-----------2')
    return check_time  # 返回了这个并没有赋值给playgame，而是谁都没给，直接调用


@outer_check(24)  # 带参以time直接传入函数
def play_game():
    return '玩游戏'


print(play_game())
