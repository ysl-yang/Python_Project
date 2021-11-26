# -*- coding: UTF-8 -*-
'''
    关键字驱动
    1.common启动程序，将常用的方法 取消、跳过、确定，读取yaml方法等写在公共文件common，
    2.取消、跳过会用到点击事件，将元素定位、对元素的操作封装到baseView类中，关键字驱动类
    3.登录页面、查询页面、流程页面，使用pom进行页面管理
    4.测试用例，使用unittest或pytest管理测试用例
    5.data文件，用来管理测试数据
'''
import time

from appium import webdriver


class BaseView:
    def __init__(self, driver):

        self.driver = driver

    # 元素定位
    def loctor(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def on_input(self, loc, txt):
        self.loctor(loc).send_keys(txt)

    # 点击
    def on_click(self, loc):
        self.loctor(loc).click()

    # 强制等待
    def wait(self, time_):
        time.sleep(time_)

    # 关闭
    def close(self):
        self.driver.quit()

    # 获取窗口大小
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动
    def swipe(self, start_x, start_y, end_x, end_y, t):
        self.driver.swipe(start_x, start_y, end_x, end_y, t)
