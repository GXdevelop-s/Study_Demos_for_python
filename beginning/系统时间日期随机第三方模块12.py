# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年11月26日
"""
import datetime
import time
import sys
import random
import hashlib
import requests

'''
当导入模块的时候，模块搜索路径存储在system模块的sys.payh变量中，变量里包含当前目录，pythonpath和由安装过程决定的默认目录
当文件夹变蓝（可以右键标记为蓝色）的时候,就会被加入到搜索路径当中，这在大项目中比较有用
系统模块：
    sys模块
    time与datetime
    random
第三方模块：
'''

print(sys.path)
print(sys.version)
print(sys.argv)  # 在cmd中工作目录下 python 文件名 命令 后可以加参数，或者在右上角edit configuration中parameters里面进行传参，
# 主要用于执行的时候从外界传参数进来argv是一个列表

# time模块
# 1.时间戳
t = time.time()  # 一个浮点型的秒数
print(t)
time.sleep(1)
t1 = time.time()
print(t1 - t)  # 用时间戳的差值来计算程序运行的时间

# 将时间戳转成字符串
s = time.ctime(t)
print(s)  # 年月日时分秒
# 将时间戳转成元组的形式（还有反向）
t = time.localtime(t)
print(t)
print(t.tm_year)  # 以元组的方式得到某个年、月等等
t = time.mktime(t)  # 反向

# 自定义时间格式(将元组转成字符串)
s1 = time.strftime('%Y-%m-%d %H:%M:%S')  # 取当前的时间按照自定义格式控制变成字符串
print(s1)

# 反向自定义时间格式（字符串转换成元组）
r = time.strptime('2019/06/20', '%Y/%m/%d')
print(r)

# datetime:time模块升级版
'''
datetime模块：
以下四个都是类
    time  时间   
    date    日期（data数据）
    datetime 日期时间
    timedelta 时间差 
'''
d = datetime.date(2019, 6, 20)

print(d.today())  # 当前的日期 2021-11-26，虽然是date对象在调用，但是
print(datetime.date.ctime(d))  # 对象的具体时间  Thu Jun 20 00:00:00 2019，必须要参数
print(datetime.date.today())  # 当前的日期 2021-11-26 其中封装了time.time()

# datetime,timedelta
'''
表示两个datetime对象的不同
需要和时间结合使用
'''
timedel = datetime.timedelta(hours=2)  # 给了个小时的时间差值
print(timedel)
now = datetime.datetime.now()  # 得到当前时区的时间 从年到秒
result = now - timedel  # 得到两个小时之前的时区时间从年到秒 timedelta对象支持+-操作
print(result)
# 应用点： 缓存：数据redis 作为缓存 redis.set(key,value,时间差)，过了时间差就删除  会话：session


# random模块
ran = random.random()  # 0~1之间的随机小数
print(ran)
ran = random.randrange(1, 10, 2)  # 从1-9，步长为2的的随机数（即1，3，5，7，9中一个随机int）
print(ran)
ran = random.randint(1, 10)  # 不多bb
print(ran)
list1 = ['a', 'b', 'c', 'd']
ran = random.choice(list1)  # 在list1中随机选择
print(ran)
list2 = ['a1', 'b1', 'cc', 'dd']
random.shuffle(list2)  # 洗牌方法没有返回值，只对list2本身操作(随机打乱)
print(list2)

# hashlib  加密算法：md5 sha256 （单项的，无法解密，除非知道如何加密的）
'''
加密算法不能直接传字符串，所有都必须编码
'''
# md5
msg = '冻手冻手，准备干台湾'
S_msg = hashlib.md5(msg.encode('utf-8'))  # 按照utf-8的方式进行编码，返回值是是一个md5的对象
print(S_msg.hexdigest())  # 取出16进制的表示方式

# sha256
msg1 = '冻手冻手，准备干台湾'
S_msg = hashlib.sha256(msg1.encode('utf-8'))
print(S_msg.hexdigest())

msg2 = '先打莲花机场'
S_msg = hashlib.sha256(msg2.encode('utf-8'))
print(S_msg.hexdigest())  # 越长的加密结果就说明加密的算法越严密
# 因为加密不可逆，所以把输入的密码也加密，与数据库中加密保存的密码来进行判断


# 第三方模块：pillow
'''
依赖pip进行安装
处理图片的第三方模块
在terminal中执行 pip install pillow,安装第三方库
requests 模拟浏览器的模块
就是代替浏览器的一些操作
'''
respond = requests.get('http://www.baidu.com/')  # 向百度网址发送请求，
print(respond.text)
