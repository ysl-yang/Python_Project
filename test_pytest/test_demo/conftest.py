# -*- coding: UTF-8 -*-
'''
    setup,threadown的配置文件
scope参数定的4中等级（默认是function）,文件名称一定是conftest.py
    session：测本次session级别中只执行一次
    module：在模块级别中只执行一次
    class：在类级别中只执行一次
    function：在函数界别中执行，每有一个函数就执行一次
'''
import pytest


# 定义一个基本的setup和threadown
# 预置函数
@pytest.fixture(scope='function')
def test_demo1():
    print('哈哈哈哈哈')
