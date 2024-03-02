# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年10月23日
"""
# ori_path F:\pythonfiles\other corresponding files\ori
# new_path F:\pythonfiles\other corresponding files\new
import os

ori_path = r'F:\pythonfiles\other corresponding files\ori'
new_path = r'F:\pythonfiles\other corresponding files\new'


def copy(ori_path, new_path):
    if os.path.isdir(ori_path):
        os.mkdir(new_path)
        files = os.listdir(ori_path)
        for file in files:
            copy(os.path.join(ori_path, file), os.path.join(new_path, file))
    else:
        with open(ori_path, 'rb') as r_stream:
            container = r_stream.read()
            with open(new_path, 'wb') as w_stream:
                w_stream.write(container)


try:
    copy(ori_path, new_path)
except Exception as err:
    print('主要的问题在', err)
else:
    print('完成操作')
finally:
    print('程序结束')
