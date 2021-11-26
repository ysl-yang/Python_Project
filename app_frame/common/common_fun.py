# -*- coding: UTF-8 -*-
'''
    动作：跳过、取消
'''
from selenium.webdriver.common.by import By

from app_frame.baseView.baseView import BaseView
from app_frame.common.desired_caps import appium_desired


class Common(BaseView):
    # 取消
    cancel = (By.ID, 'android:id/button2')
    # 跳过
    skip = (By.ID, 'com.tal.kaoyanid/tv_skip')
    # 确定
    sure = (By.ID, 'android:id/button1')

    def check_cancel(self):
        print('===点击取消===')
        try:
            self.on_click(self.cancel)
        except Exception as e:
            print('===没有取消按钮===')

    def check_skip(self):
        print('===点击跳过===')
        try:
            self.on_click(self.skip)
        except Exception as e:
            print('===没有跳过按钮===')

    def check_sure(self):
        print('===点击确定===')
        try:
            self.on_click(self.sure)
        except Exception as e:
            print('===没有确定按钮===')

    # 获取窗口大小
    def get_size(self):
        x = self.get_window_size()['x']
        y = self.get_window_size()['y']
        return x, y

    # 滑动
    def swipe_left(self):
        l = self.get_size()
        x1 = l[0] * 0.9
        y1 = l[0] * 0.5
        x2 = l[0] * 0.2
        self.swipe(x1, y1, x2, y1, 1000)


if __name__ == '__main__':
    # 启动程序
    driver = appium_desired()
    com = Common(driver)
    com.check_cancel()
    com.check_skip()
