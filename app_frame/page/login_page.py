# -*- coding: UTF-8 -*-
'''
    封装登录内容
'''
from selenium.webdriver.common.by import By

from app_frame.common.common_fun import Common
from app_frame.common.desired_caps import appium_desired


class LoginView(Common):
    # 登录元素
    # 用户名
    # 密码
    # 按钮
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    login_btn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    # 点击“我的”
    myself = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    # 获取用户信息
    userinfo = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    # 设置
    set_in = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    # 退出
    out = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    # 登录流程
    def login(self, username, password):
        # 取消
        self.check_cancel()
        # 跳过
        self.check_skip()
        # 确定
        # self.check_sure()
        # 传入用户名
        self.on_input(self.username_type, username)
        # 传入密码
        self.on_input(self.password_type, password)
        # 点击登录
        self.on_click(self.login_btn)
        self.wait(5)

    # 检测登录状态的方法
    def login_status(self):
        try:
            self.on_click(self.myself)
            self.loctor(self.userinfo)
        except Exception as e:
            print('登录失败')
            return False
        else:
            print('登录成功')
            return True

    # 退出登录
    def login_out(self):
        self.on_click(self.set_in)
        self.on_click(self.out)
        print('退出成功')


if __name__ == '__main__':
    driver = appium_desired()
    lo = LoginView(driver)
    lo.login('qwerty2664', 'qwerty123')
