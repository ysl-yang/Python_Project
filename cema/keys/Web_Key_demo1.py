from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from cema.keys.chrome_options import ChromeOptions
from log_demo1 import test_log

log = test_log()


# 基于type_值决定生成的driver对象是什么类型
def open_browser(type_):
    if type_ == 'Chrome':
        driver = webdriver.Chrome(options=ChromeOptions().options())
    else:
        try:
            driver = getattr(webdriver, type_)()
        except Exception as e:
            print("Exception Information:" + str(e))
            driver = webdriver.Chrome()
    return driver


class WebKeyDemo1:

    # 构造函数
    def __init__(self, txt):
        self.driver = open_browser(txt)
        self.driver.implicitly_wait(10)

    # url
    def url(self, txt):
        log.info('打开网址{}'.format(txt))
        self.driver.get(txt)

    # 定位
    def location(self, name, value):
        log.info('这是{}定位,定位元素{}'.format(name, value))
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, txt):
        try:
            log.info('这是{}定位,定位元素{},输入信息{}'.format(name, value, txt))
            self.location(name, value).send_keys(txt)
        except Exception as e:
            log.error('输入异常%s' % e)

    # 点击
    def click(self, name, value):
        try:
            log.info('这是{}定位,定位元素{}'.format(name, value))
            self.location(name, value).click()
        except Exception as e:
            log.error('定位异常%s' % e)

    # 退出浏览器
    def quit(self):
        log.info('退出浏览器')
        self.driver.quit()

    # 强制等待
    def sleep(self, txt):
        sleep(txt)

    # 窗口最大化
    def max_win(self):
        self.driver.maximize_window()

    # 显示等待
    def wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.location(name, value), message='等待失败')

    # 断言
    def assert_text(self, name, value, txt):
        try:
            reality = self.location(name, value).text
            assert txt == reality, '断言失败，实际结果为：{}'.format(reality)
            log.info('断言失败，实际结果为：{}'.format(reality))
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            return False


'''
    # 断言文本
    def assert_txt(self, name, value, expect):
        try:
            assert expect == self.location(name, value).text, '断言失败'
            return True
        except:
            return False
'''
