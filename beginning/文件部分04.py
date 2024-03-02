# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月20日
"""
'''
读：
    open(path/filename,mode)    -----返回值：stream对象（管道）,注意mode默认是 rt，如果读其他文件的化，需要改为rb， b--binary
    stream.read()   ----读取管道中的内容,mode指明了管道的类型
'''
stream1 = open(r'F:\pythonfiles\other corresponding files\t1.txt', mode='r')  # r是防止'    '里面反斜杠转义字符的，
containers = stream1.read()
print(containers)
print(stream1.readable())  # 判断是否可读

line = stream1.readline()  # 这里的 readline读不出来任何东西，因为上面的read已经把这个流里边的东西都拿走了； 每读一行都会加一个\n，相当于是加了两个换行
lines = stream1.readlines()  # 把内容保存在列表中了
stream1.close()  # 关闭管道

'''
写文件
stream2 = open(filename, mode='w')      如果文件不存在就自动创建
只要mode是w就表示是写操作
方法： write（内容）      ---将原来的内容清空，再写当前的部分
                        ---将mode改成'a'--append,就可以追加了
    writelines（Iterable）--- 没有换行效果
'''

stream2 = open(r'F:\pythonfiles\other corresponding files\t2.txt', mode='w')
strs = '''
hi xu:
    welcome to manchester united !
    we are happy to see you being a part of us
                                your future team

'''
result = stream2.write(strs)
print(result)  # 返回值是int
stream2.writelines(['c罗\n', '林皇\n', 'b费\n'])  # 换行效果要自己加
stream2.close()  # 关闭管道

'''
复制文件
用 with as 语句自动化
open只能用来打开文件，不能对整个文件夹（目录）操作 -----
所以引入os模块---- operating system interfaces
'''
with open(r"F:\pythonfiles\other corresponding files\EEbf4-BXkAAhuMQ.jfif", 'rb') as rstream:  # 加载到流
    container = rstream.read()
    with open(r"F:\pythonfiles\other corresponding files\copypicture1.jpg", 'wb') as wstream:
        wstream.write(container)  # 流输出完成复制
print("完成复制")

'''
os模块使用（需要import导入）
获取路径
一个py文件就相当于一个模块，python在扩展包中有需要内置模块
截取文件名
'''
import os  # pep8要求import要放在最上面，这里为了方便

nowpath = os.path.dirname(__file__)  # 获取当前文件的文件目录（绝对路径）
print(type(nowpath))  # 以字符串的方式返回
print(nowpath)
newpath = os.path.join(nowpath, 'a1.jpg')  # 在当前路径下（文件目录下）拼接了一个文件名,返回值是新路径，起到整合文件名的作用,允许跟多个
only_file_name = newpath[newpath.rfind('\\') + 1:]  # 用字符串截取到文件的名字

'''
os模块中的方法
'''

# path.isabs() 判断是否是一个绝对路径
# 绝对路径和相对路径
'''
是以盘符为基准一层层找的
rF:\pythonfiles\other corresponding files\ t2.txt
相对路径是以当前py文件为基准点，是从同级文件开始写
../  表示返回当前文件的上一级，有几级用几次
'''

# 通过相对路径得到绝对路径 参数是相对路径，返回值为绝对路径
abspath = os.path.abspath('练习.py')
print(abspath)

# 获取当前文件的绝对路径
nowabspath = os.path.abspath(__file__)
nowabs_folder = os.getcwd()  # 获取当前文件夹（目录的）绝对路径
sbsmulu = os.path.isdir(os.getcwd())  # 判断一个对象是否为一个目录

# os.path.split()  ----将一个绝对路径的目录和文件名分隔开，返回一个含有两个元素的元组
# os.path.splitxet() ----将一个绝对路径的扩展名隔开，元组返回一个
an_ordinary_path = os.path.abspath(__file__)
splited_result = os.path.split(an_ordinary_path)
print(splited_result[1], '\n', splited_result[0])

# os.path.getsize(path) ----获取文件大小 单位字节
size = os.path.getsize(__file__)
print('文件的大小为{}字节'.format(size))

# os.listdir(path)  # 返回指定目录下的所有文件和文件夹，保存到列表里面
allfiles = os.listdir(r'F:\pythonfiles\PycharmProjects\startdemo\beginning')
print(allfiles)

#  os.mkdir(path) ---创建一个路径为path的文件夹
#  os.path.exists(path) ---判断文件是否存在（布尔类型返回值）
#  os.rmdir(path)   ---删除文件夹（只能删除空的文件夹）
if not os.path.exists(r'F:\delete_me'):
    os.mkdir(r'F:\delete_me')
os.rmdir(r'F:\delete_me')
print('操作成功！')

# os.removedirs(path)   ---删除多级目录,如果子文件删除成功才尝试删除父文件（要删除的目录必须是空目录）
os.removedirs(r'F:\delete_me\hsk')

# os.remove(path)   ---删除文件（只能是一个文件 ）
os.remove(r'F:\delete_me\hsk\a1.txt')

# os.chdir()    ---切换目录
os.chdir(r'F:\delete_me')
print(os.getcwd())  # 得到的当前目录就是切换的目录了
