# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年08月01日
"""
# for i in range(3):
#     print(i)  # 遵循PEP8，每一个缩进是四个空格
# # 变量的命名不需要声明
# money = 100  # int
# money1 = 'cl'  # 都str，单双引号搭配表达里面有意义的引号
# money2 = "cl"
# money3 = '''cl'''  # 三引号保留格式
# money4 = '''
#             1
#     2222           3333
# '''
# print(money4)
# receive = input('请输入')  # 输入函数input

# 类型转换和c一样  注意带小数点的 字符串不能转int类型   只有0和空字符串的布尔值为false，其他的都是
print(1, 2, 3, sep='#')  # 说明逗号输出用’#‘， 默认end='\n'
print('*' * 20)  # 表示打印20个'*'
# '/'表示除法，'//'表示整除,'**'表示次幂，还多了'//='和'**='其他的运算和c一样
# 比较运算符和c++一样，多了is（地址)
score = 85
print(60 <= score <= 90)  # python是可以按照这种数学方式去写的
# 逻辑运算符and or not,比较运算符>逻辑运算符（not>and>or）
age = 10
print('我今年' + str(age) + '岁了')  # 字符串之间可以用'+'进行拼接
# 格式化输出
age = 10
name = 'xu'
print('我喜欢听%d岁的%s唱歌' % (age, name))  # 只占一个位置可以不用加括号，数位控制和c一样，%s会强制转换
# bin函数可以转换成2进制，oct函数转8进制，hex函数转16进制，且参数进制不限  0b开头二进制，0o开头八进制，0x开头十六进制，默认十进制（字面量）
# ps：转十进制用int就行
# 位运算（针对二进制来说的） &和and差不多；|和or差不多；^异或运算符，二进制相异为真；~取反码；<<向左移（头两位没了），移动几位就乘以2的几次方；>>向右移（后两位没了），除以2的几次方
print(int(0b1001))