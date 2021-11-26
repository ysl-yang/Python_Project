from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class WebKeys:
    driver = webdriver.Chrome()

    # URL
    def url(self, name):
        self.driver.get(name)

    # 窗口最大化
    def max_widonws(self):
        self.driver.maximize_window()

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 定位
    def location(self, name, value):
        return self.driver.find_element(name, value)

    # 点击
    def click(self, name, value):
        self.location(name, value).click()

    # 输入
    def input(self, name, value, txt):
        self.location(name, value).send_keys(txt)

    # 强制等待
    def sleep(self, sleep_):
        sleep(sleep_)

    # 显示等待
    def wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.location(name, value), message='等待失败')

    # 获取句柄
    def current_win_han(self):
        return self.driver.current_window_handle
