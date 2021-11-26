# -*- coding: UTF-8 -*-
from time import sleep

import pytest
from selenium import webdriver


def test_01():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    sleep(2)
    driver.quit()


def test_02():
    driver = webdriver.Chrome()
    driver.get('https://www.bilibili.com/')
    sleep(2)
    driver.quit()


if __name__ == '__main__':
    pytest.main(['test_case2.py', '-n', '2'])
