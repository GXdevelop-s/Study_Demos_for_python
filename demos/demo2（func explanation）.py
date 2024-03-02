# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年09月25日
"""


def islogin(username='7', password='8'):
    '''
    denglu
    :param username:
    :param password:
    :return:
    '''
    if username == 'f1' and password == '123':
        return True
    else:
        return False


def borrow_book(bookname):
    '''
    jieshu
    :param bookname:
    :return:
    '''
    if islogin(input('用户名：'), input('密码')):
        print('成功借阅{}'.format(bookname))
    else:
        print('还未登录，不能借书')


borrow_book('s')
