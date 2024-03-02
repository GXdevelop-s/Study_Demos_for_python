# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月24日
"""
import os

# 异常处理01
'''
格式：
try:
    可能出现异常的代码
except 异常类型1:                    ---后面要跟错误类型
    如果有异常执行的代码1
except 异常类型2:                    ---多个except
    如果有异常执行的代码2    
[finally:
    无论是否存在异常都会执行的代码]
    
'''


def func():
    n1 = int(input('输入第一个数字'))
    n2 = int(input('输入第二个数字'))
    # + 加法
    sum = n1 + n2
    print('和是', sum)


# 分析：有可能输入的不是数字，但程序不能崩，所以要有异常处理
def func2():
    try:
        n1 = int(input('输入第一个数字'))
        n2 = int(input('输入第二个数字'))
        # 除法
        sum = n1 / n2
        print('和是', sum)
    except ZeroDivisionError:
        print('除数不能为零')
    except ValueError:
        print('必须输入数字')
    except Exception:
        print('出错啦')


# 异常处理树形结构
'''
在产生异常时，产生的异常类型就会和except就会和except匹配
匹配的顺序是从上到下，匹配的原则是能匹配就匹配
所以最大的except要放在最后
exception是最大的，所以和谁都能匹配
不知道什么原因也可以用：
except Exception as err:
    print('原因是',err)
'''


def func3():
    try:
        n1 = int(input('输入第一个数字'))
        n2 = int(input('输入第二个数字'))
        # 除法
        sum = n1 / n2
        print('和是', sum)
        print('运行')
        with open(r'f:\c2.txt', 'r') as stream:
            stream.read()
    except ZeroDivisionError:
        print('除数不能为零')
    except ValueError:
        print('必须输入数字')
    except Exception as err:  # 报错的原因是 FileNotFound
        print('出错啦,原因是：', err)


# 异常处理02
'''
格式：
try:
    可能出现异常的代码
except 异常类型1:                    ---后面要跟错误类型
    如果有异常执行的代码1
except 异常类型2:                    ---多个except
    如果有异常执行的代码2    
else:
    如果try中没有发生异常则进入的代码（如果try中有return就没法到达）
'''

# 异常处理03
'''
finally的具体用法
'''


def func4():
    stream = None
    try:
        stream = open(os.path.abspath(__file__), 'r')
        container = stream.read()
        print(container)
        return 1  # 后面还有finally，这里不会return
    except Exception as err:
        print(err)
        return
    finally:
        print('-----Finally------')
        if stream:
            stream.close()
        return 3  # 覆盖了原来的return值1（如果没return就返回1）


# 抛出异常
'''
raise
'''


def register():
    admin = input('输入用户名')
    if len(admin) < 6:
        raise Exception('用户名必须小于6位')  # 这里原本应该是通过本来的错误来抛出的，在此先借用它的父类来完成
    else:
        print('输入的用户名是', admin)


try:
    register()
except Exception as err:
    print(err)
else:
    print('注册成功')
