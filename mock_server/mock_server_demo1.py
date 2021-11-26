# -*- coding: UTF-8 -*-
# 实现mock的生成与调用
from unittest import mock


# 伪造一个接口函数
def sum(a, b):
    # return a + b
    pass


def login():
    print('登录成功')


# print(sum(1, 2))
'''
    mock.Mock，定义函数的返回值，无关乎函数本身内容，直接写入最终的返回值结果
'''
# sum = mock.Mock(return_value=18)
# print(sum(1, 2))
login()
