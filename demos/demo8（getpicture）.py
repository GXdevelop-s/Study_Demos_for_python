# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月03日
"""
import re

import requests

# 先拿到标签
path = '<img src="https://pics4.baidu.com/feed/810a19d8bc3eb135db732b1f3c342bdafc1f4496.jpeg?token=cc425e4d816ead5456ab9491eb82a9a1" width="640" class="_3yZQZ9OxCCD0QVw16rnEsS">'
# 再通过正则拿到图片链接
r = re.match(r'\A<img src="(.+)">', path)
print(r.group())
print(r.group(1))
# 向该链接发送获取请求
r1 = requests.get(r.group(1))
# 查阅requests文档，如果不是text而是其他的格式可以用content，会自动转换
with open('del.jpg', 'wb') as stream:
    stream.write(r1.content)
