# -*- coding: UTF-8 -*-
import pytest
import allure


@allure.feature('用例描述测试需求的情况')
@allure.story('用户访问首页的情况下')
@allure.title('测试01用例名称')
def test_01():
    print('-----------------')
    print('test01')


def test_02():
    print('-----------------')
    print('test02')


# 通过装饰器，当该用例报错时重新运行3次，间隔时间3秒
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_03():
    print('-----------------')
    print('test03')
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(['test_case3.py', '-s', '-v', '--alluredir ./result'])
    # 第一次用例执行后，第二次执行第一次失败的用例
    # --lf 只运行上一次失败的用例，--ff 先运行失败的用例再运行其他用例
    # pytest.main(['-s', '--lf', 'test_case3.py'])
    # --reruns=3 失败重新运行的次数，--reruns_delay=3 重新运行的间隔单位为秒
    # pytest.main(['-s', '--reruns=3', '--reruns-delay=3', 'test_case3.py'])
