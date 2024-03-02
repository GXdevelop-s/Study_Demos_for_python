# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年11月28日
"""
# 正则表达式的概念
'''
正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符及字符组合，组成一个“规则字符串”
就是对字符串合法性的验证

作用特点：
    1.给定的字符串是否符合正则表达式的过滤逻辑（叫做匹配）

'''

# python re模块
import re

msg = 'whoismybaby'
pattern = re.compile('mybaby')  # 编译一个正则格式，返回一个pattern对象
result = pattern.match(msg)
print(result)  # 没有匹配到返回空，conpile是从头开始匹配的

# 真正的正则 使用re方法：match
'''
注意：正则永远验证的是字符串
match底层封装了pattern
'''
result = re.match('mybaby', msg)
print(result)  # 不成功返回None

# search
'''
进行正则字符串匹配方法，匹配的是整个字符串（拿着正则去找）
返回一个匹配对象，span为位置，match为匹配的内容部分
'''
result = re.search('mybaby', msg)
print(result)
print(result.span())  # 返回位置
print(result.group())  # 使用group提取到匹配的内容
print(result.groups())  # ???

# 正则符号 7b 8k
'''
刚才是给死的表达式
现在要给一个范围或者
[]表示一个范围，里面是要匹配的内容，范围里的任意字符匹配到就行
search的正则表达式要按照整体看，search找到一个就不继续了——可以用findall方法
'''
msg1 = 'abas1ssaj3hsa7ff00'
result = re.search('[0-9][a-z]', msg1)  # 要求必须数字挨着字母，这是按整体看的
print(result.group())

# findall
'''
一直找到头
'''
result = re.findall('[0-9][a-z]', msg1)
print(result)  # findall返回由找到结果的字符串

# 正则符号  a8b  a88a a789a
'''
'*' 用于将前面的模式匹配0次或者多次，贪婪模式
'+' 用于将前面的模式匹配1次或者多次(至少一次)，贪婪模式
'？'用于将前面的模式匹配0次或者1次,贪婪模式 0，1
'*?,+?,??' 即上面三种特殊字符的非贪婪模式（尽可能少的匹配）

'''
msg2 = 'dsaj1222jghj2gui1i2gu3iu2g333g'
result = re.findall('[a-z][0-9]+[a-z]', msg2)
print(result)
# qq号码验证5~11 开头不能是0
f'''
'.' 用于匹配除换行符（\n）之外的所有字符
'^' 用于匹配字符串的开始，即行首
'$' 用于匹配字符串的末尾（末尾如果有换行符\n，就匹配\n前面的那个字符），即行尾

'''
# '{m}'用于将前面的模式匹配m次，'{m,}'用于验证将前面的模式匹配m次或者多次>=m
# '{m,n}' 用于将前面的模式匹配m次到n次（贪婪模式），最大匹配n次，'{m,n}?'即为上面的贪婪版本
qq = '1494468'
result = re.match('[1-9][0-9]{4}', qq)  # 这个时候也是可以匹配成功的，匹配到了字符串的前五位，但是我们希望是拿整体去匹配的
print(result)  # 匹配成功
result = re.match('^[0-9][1-9]{4}$', qq)  # 拿正则和整个开头结尾进行匹配
print(result)  # 匹配不成功
result = re.match('^[0-9][1-9]{4,10}$', qq)
print(result)  # 按照要求匹配成功

# 正则预定义
# \A 表示从字符串的开始处匹配
# \Z 表示从字符串的结束处匹配，如果存在换行，只匹配到换行前的结束字符串
# \s 匹配任意空白字符，等价于[\t\n\r\f]   \S 匹配任意非空白字符 等价于[^\s]
# \b 匹配一个单词边界 也就是指单词和空格间的位置  \B匹配非单词边界
# \d 匹配任意数字，等价于[0-9]  \D 匹配任意非数字字符，等价于[^\d]
# w\ 匹配任意字母数字及下划线，等价于[a-zA-Z0-9_]  \W 匹配任意非字母数字及下划线 等价于[^\w]
#  \\ 匹配原义的反斜杠

# 用户名可以是字母或者数字下划线，不能是数字开头，用户名长度必须在6-12位
admin = 'admin006'
result = re.match(r'\A\D\w{5,11}$', admin)
print(result)
# 取出所有的文件名
names = 'x1.txt x2.txt x3txt x4txtx5txt'
result = re.findall(r'\D\w+\.txt\b', names)  # 这里注意，用findall的时候，不能锁死头尾  .要转义两次
print(result)

# 分组
'''
[]中每一个字符都是一个个体，|也是一个个体  ————  []只占一位
（）中|可以分割成不同的整体个体  ———— （）占一块
'''
# 匹配数字0-100数字
n = '100'
result = re.match(r'[1-9]?\d?$|100$', n)  # |为或者，加两个$符号来分段匹配
print(result)
# 验证邮箱 163 126 11
email = '1785598676@qq.com'
result = re.match(r'\w{5,20}@(163|126|qq)\.(com|cn)', email)
print(result)
# 邮箱不以0开头   [^0]代表除0之外的所有字符
result = re.match(r'[^0]\w{4,19}@(163|126|qq)\.(com|cn)', email)
print(result)

# 爬虫
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result)
# 分别提取
print(result.group())
# （）表示分组  result.group(n)拿到第n组中的内容  还可以结合|来使用
print(result.group(1))  # 表示提取到第一组的内容
print(result.group(2))
# 爬标签
msg3 = '<html>abc</html>'
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$', msg3)  # \1表示引用第一组中拿到的东西,达到前后的引用匹配
print(result)
print(result.group(1))

# 起名的方式  (?P<name1>正则)  (?P=名字)
msg4 = '<html><h1>qqq</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>',
                  msg4)  # 括号里面 ？P<name>  的写法就是起名字， ？P=name就是引用前面的组
print(result)

# re sub
'''
替换
sub(正则,'新内容',string)
sub(正则,函数,string)
'''
result = re.sub(r'\d+', '95', 'java:99 python 100')
print(result)


def func(temp):
    num = int(temp.group())  # 拿过来是字符串，记得类型转换
    num1 = num - 1
    return str(num1)  # 扔出去是字符串，记得类型转换


result = re.sub(r'\d+', func, 'java:99 python 100')  # 每找到一个替换的内容，拿过来处理再抛出去
print(result)

# re split
'''
切割
按照正则匹配到的为界切一刀，匹配到了就切
'''
result=re.split(r'[,:]', 'java:99 ,python 100')
print(result)  # 返回列表
