from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class WebShop:
    driver = webdriver.Edge()

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 窗口最大化
    def max_win(self):
        self.driver.maximize_window()

    # 强制等待
    def sleep(self, time):
        sleep(time)

    # 显示等待
    def wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.location(name, value), message='等待失败')

    # url
    def url(self, name):
        self.driver.get(name)

    # 定位
    def location(self, name, value):
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, txt):
        self.location(name, value).send_keys(txt)

    # 点击
    def click(self, name, value):
        self.location(name, value).click()
