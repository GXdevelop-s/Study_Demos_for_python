# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年08月03日
"""
# 缩进代表范围
import random  # 呼叫一个随机数的库
import time

x = random.randint(1, 10)  # 1到10的随机数
if int(input('输入你猜的数字')) == x:
    print('yes')
    pass  # 没有实际意义只是支撑结构
elif int(input('输入你猜的数字')) == 5:
    print('no5')
elif int(input('输入你猜的数字')) == 6:
    print('no6')
else:
    print('no')
# 三元运算符
# b = 1
# c = a if a > c else c = b  # 条件成立执行前面的，不成立执行后面的
# while                 break和continue依然成立
n = 1
while n < 10:
    print(n)
    n += 1
# for
for i in range(1, 11, 2):  # range是封装好的，产生一个列表，也可以把range换成字符串或者是其他的列表
    print(i)
# for else语句 同理还有while else语句，特点一样
# for i in range(n+1):
#     循环体
# else:                     n次循环执行到头没有break，则执行else
#     语句

# id函数得到字符串地址，is运算符判断两个地址是否相等
# python为了节省内存，只要是内存池有过的字符串，无论拿多少次都是一个地址
# 字符串索引机制： 1. 0~len（）-1   2.  -len（）~-1 （包前不包后）            两套规则可以交叉使用
# 字符串切片
s = 'ABCDEFGH'
s1 = s[1:4]  # 索引包前不包后
s2 = s[:4]  # 默认从0开始
s3 = s[1:]  # 默认到最后
s4 = s[:-1:2]  # 步长为2   step为正说明从左往右，负数为从右往左
print(s1)
print(s4)
# 字符串函数
# （r）find:从（右）左向右（左）查找，返回 位置索引，无则-1，还可以放一个词，返回首字母位置
# r（index）:和find一样只不过找不到会报错
# count：统计字符个数

# 判断字符串函数（返回值都是布尔类型的）
# startwith：以谁开头  endwith：以谁结尾    isalpha:是不是全字母      isdigital：是不是全数字  isalnum：是不是只有数字和字母
# isspace：是不是空白字符串  isupper islower：大小写

# 字符串替换切割修改
# replace（old，new，count）：三个参数，old，new，替换的个数（默认全部替换）
# 切割 （r）split（'要搜索的分隔符'，count）：分割后会将其变成一个列表，只是切割的方式不一样了，count最多切几刀，不改变格式
#     splitlines（）：按行来切割（针对有格式的字符串），变成列表
#     partition（''）：按分隔符切一道，变成一个三元组，左，分隔符，右，三部分
# 修改：
#     title：每个单词首字母变大写
#     upper：都变大写  lower同理
#     capitalize：一句话第一个单词变大写

# 字符串空格和拼接
# 去空格   （l/r）strip:（左/右）全空格清楚
# 添加空格   center（count）：给定count个字符，把字符串放在中央
#         （l/r）just(count):把字符串放在(左/右)
#
# #格式化
# 1.%s %d....
# 2.格式化
age = 17
name = 'wxt'
result = '{}岁的{}'.format(age, name)
print(result)
# 使用数字填充，从0开始
result = '{0}岁的{1}和{0}的我'.format(age, name)  # age是0，name是1
# 变量名填充
result = '{age2}岁的{name2}和{age2}的我'.format(age2=18, name2='wxt')  # format的参数必须是关键字参数
print(result)
'#'.join([1, 2, 3])  # 用#将

# 列表
list1 = ['秀']  # 索引和切片和字符串一样

# 列表的增删改查
list1.append('6呀')  # 增
print(list1)
list2 = [6]
list1 = list1 + list2  # 列表之间合并
list1.extend(list2)  # 把list2加到list1里面
print(list1)
# 插入
list1.insert(1, 'charu')  # 在索引为1的位置（原来的0和1中间）插入

# 删除
list1.pop()  # 只能从最后删除
list1.remove('6呀')  # 根据元素值删除,如果有多个相同元素，只删除第一个；都删除要循环
# 清除
list1.clear()
print(list1)
# 指令性删除
del list[0]  # 删除索引为0的元素         ！但如果该列表已经给过一份到其他列表，del只起到断开指针指向的作用
# del list 是删除整个列表

# 查找
index1 = list1.index('charu')  # 寻找到charu这个元素的索引
list1.count('cahru')  # 查找元素的个数
# 判断元素是否在列表里  同理还有 not in
if 6 in list1:
    print('yes,bro')

# 排序
list3 = []
list3.sort()  # 默认是升序，默认 reverse=false
list3.sort(reverse=True)  # 降序
list3.reverse()  # 没有排序，只有翻转

# python特有的交换变量
a = 2
b = 3
a, b = b, a

# 冒泡排序
nums = []
for i in range(10):
    nums.append(random.randint(10, 25))
print(nums)
for j in range(0, len(nums) - 1):
    for k in range(j, len(nums) - 1):
        if nums[k] > nums[k + 1]:
            nums[k], nums[k + 1] = nums[k + 1], nums[k]
print(nums)

# 元组
# 元组与列表类似，不同在于元组的元素不能修改（增删改），元组用小括号，列表用方括号
t1 = ('xu')  # 这是一个字符串
t1 = ('xu',)  # 这是一个元组，如果元组中只有一个元素，必须添加逗号，多个元素就正常了
# 下标和切片都一样，支持for in 循环
# 函数(只有)
# count（）
# index（元素,start,end）
list(tuple)  # 元组转列表
tuple(list)  # 列表转元组
time.sleep(1)  # 休眠一秒

# 字典   就相当于c++里面的队组·
dict1 = {'name': 'xu'}
print(dict1['name'])
# 修改和添加的具体操作都是赋值
dict1['name'] = 'shu'  # 修改
dict1['sex'] = 'female'  # 添加
# 删除
value = dict1.pop('name')  # 根据key值删除，返回值为key值的value
r = dict1.popitem()  # 删除最后一项，返回值是一个元组（key，value）
dict1.clear()  # 清空字典
# 还有系统自带的del，  del dict1['name']   del dict1
dict1['name'] = 'shu'  # 修改
dict1['sex'] = 'female'  # 添加
# 查询
value = dict1.get('name', 'chenshuxu')  # 取到的值是value值，如果找不到，第二给参数是默认值，一般是None
# len（）是通用的
# 遍历：如果用for in遍历字典，i取出来的是key值
# dict.value()会取出所有值封装成一个列表，它是一个列表
for i in dict1.values():
    print(i)  # 此时取出来的才是字典里面所有的value值
for i in dict1.keys():
    print(i)  # 此时取出来的是字典里面所有的key值
# 按对取出
for k, v in dict1.items():  # item()会把字典变成 列表中的元组 这样的格式  eg：  [('name','shu'),('sex','female')]
    print(k, v)
    #  这种kor的方式 相当于  k,v=('name','shu')
dict2 = {'gf': 'lsy'}
# 字典合并
dict1.update(dict2)  # 将dict2加到dict1上去
# 用类的方法构建一个新的字典
dict1.fromkeys(['x', 'y', 'z'], 1)  # 让一个列表作为key值来

# 集合
set
# 特点：没有重复，无序的————将列表强转成集合可以起到取出重复元素的作用
# 符号：{}
# {元素, 元素, 元素, 元素}
set1 = set()  # 空集合必须这么声明，否则就会是字典
# 添加元素
set1.add('jianji')
set2 = set()
set2.update(set1)  # 合并集合
# 移除
set2.remove('jianji')
set2.discard('jianji')  # 移除不存在的元素不会报错
set2.pop()  # 随机删除集合中的元素
# 清空
set2.clear()
# 集合： 交集、并集、差集
set3 = {1, }
r1 = set1.intersection(set3)  # &交集     set1&set3
r2 = set1.union(set3)  # | 并集           set1|set3
r3 = set1.difference(set3)  # - 差集      set1-set3      结果是set1中不同的部分，主要看是谁调用

# 公共方法
# 例如 max()  min()  sorted()  hex()  abs()  ord() 等的方法

# 列表推导式：最终得到的是一个列表
# 格式：[i for i in 可迭代的 if 条件]
list1 = [i for i in range(1, 21)]
# 格式2：[word.title() if word.startswith('h') else word.upper() for word in list2 ]
# 有分叉，向三目运算套就好
# 第一个i是最终的i，第二个i是迭代的
