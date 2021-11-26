# -*- coding: UTF-8 -*-
'''
    pytest中用例的管理：mark/
    可以通过mark装饰器对所有的用例进行标记，不同的标记区分进行管理
'''
import pytest


@pytest.mark.uitest
@pytest.mark.parametrize
def test01():
    print('web01')


@pytest.mark.uitest
def test02():
    print('web02')


@pytest.mark.interface
@pytest.mark.temp
def test03():
    print('interface01')


@pytest.mark.interface
def test04():
    print('interface02')


if __name__ == '__main__':
    pytest.main(['-s', 'test_case2.py'])
