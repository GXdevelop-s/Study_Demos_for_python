# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月22日
"""

'''
os模块使用
一个py文件就相当于一个模块，python在扩展包中有需要内置模块
需要import导入
'''
import os  # pep8要求import要放在最上面，这里为了方便

nowpath = os.path.dirname(__file__)  # 获取当前文件的文件目录（绝对路径）
print(type(nowpath))  # 以字符串的方式返回
print(nowpath)
newpath=os.path.join(nowpath, 'a1.jpg')     # 在当前路径下（文件目录下）拼接了一个文件,返回值是新路径
# 进行复制检验
with open(r"F:\pythonfiles\other corresponding files\EEbf4-BXkAAhuMQ.jfif", 'rb') as rstream:  # 加载到流
    container = rstream.read()
    with open(newpath, 'wb') as wstream:
        wstream.write(container)  # 流输出完成复制
print("完成复制")