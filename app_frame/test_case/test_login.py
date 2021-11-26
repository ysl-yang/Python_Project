# -*- coding: UTF-8 -*-
'''
    登录用例
'''
import unittest
from ddt import ddt, data, file_data

from app_frame.common.desired_caps import appium_desired
from app_frame.page.login_page import LoginView


@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = appium_desired()

    def tearDown(self):
        self.driver.quit()

    @file_data('../data/login.yaml')
    def test_login(self, username, password):
        lo = LoginView(self.driver)
        lo.login(username, password)
        self.assertTrue(lo.login_status(), msg='断言：登录失败')


if __name__ == '__main__':
    unittest.main()
