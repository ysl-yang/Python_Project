# -*- coding: UTF-8 -*-
import pytest


def setup_module():
    print('setup_module')


def threadown_module():
    print('threadown_module')


def setup_function():
    print('setup_function')


def threadown_function():
    print('threadown_function')


def test_2(test_demo1):
    print('测试用例2')

'''
    在class中前置后置函数的运行顺序等级
        setup class
        setup method
        setup
        teradown
        teardown method
        teardown class
'''
# pytest中class对象要以test开头
class TestDemo:
    def setup(self):
        print('setup启动')

    def teardown(self):
        print('teardown关闭')

    def test_1(self):
        print('test1')

    def test_2(self):
        print('test2')


if __name__ == '__main__':
    pytest.main(['-s'])
