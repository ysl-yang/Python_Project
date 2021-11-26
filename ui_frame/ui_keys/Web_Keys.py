'''
    关键字驱动类
'''
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from ui_frame.my_conf import log_conf
from ui_frame.my_conf.chrome_options import ChromeOptions
import logging.config


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


class WebKey:
    # log_conf.get_log('../my_conf/log.ini')
    # 创建日志器
    # log = logging.getLogger()

    # 构造函数
    def __init__(self, txt, log):
        self.driver = open_browser(txt)
        self.log = log
        # 隐式等待
        self.driver.implicitly_wait(10)

    # url
    def url(self, txt):
        self.log.info('打开网址{}'.format(txt))
        self.driver.get(txt)

    # 定位
    def location(self, name, value):
        self.log.info('这是{}定位,定位元素{}'.format(name, value))
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, txt):
        try:
            self.log.info('这是{}定位,定位元素{},输入信息{}'.format(name, value, txt))
            self.location(name, value).send_keys(txt)
        except Exception as e:
            self.log.error('输入异常%s' % e)

    # 点击
    def click(self, name, value):
        try:
            self.log.info('这是{}定位,定位元素{}'.format(name, value))
            self.location(name, value).click()
        except Exception as e:
            self.log.error('定位异常%s' % e)

    # 退出浏览器
    def quit(self):
        self.log.info('退出浏览器')
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

    # 句柄切换，传入角标切换句柄
    def switch_handle(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    # 鼠标点击并悬停
    def mouse_hold(self, url):
        btn = self.driver.find_elements_by_xpath(url)[0]
        action = ActionChains(self.driver)
        action.click_and_hold(btn).perform()

    # 窗口切换
    def change_window(self, n):
        # 获取句柄
        handles = self.driver.window_handles
        # 切换到原始页面,n = 0
        # 切换句柄到第二个页面,n = 1 ,以此类推
        self.driver.switch_to.window(handles[n])
        print(self.driver.title)

    # 显示定位的地方，确定定位问题
    def locator_station(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid green;"  # 边框border:2px; red红色
        )

    # 句柄的切换（考虑不同场景的不同切换）
    def switch_handle_1(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # iframe切换default窗体
    def switch_default(self):
        self.driver.switch_to.default_content()

    # 切换frame
    def change_frame(self, a):
        self.driver.switch_to.frame(a)

    # 文本断言
    def assert_text(self, name, value, expect):
        try:
            reality = self.location(name, value).text  # 获取元素定位的文本
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            self.log.exception('断言失败，预期结果为：{0}，实际结果为：{1}'.format(expect, reality))
            # print('断言失败信息：' + str(e))
            return False

    # 属性断言
    def assert_attr(self, name, value, txt, expect):
        try:
            reality = self.location(name, value).get_attribute(txt)  # 获取元素定位的文本
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            self.log.exception('断言失败，预期结果为：{0}，实际结果为：{1}'.format(expect, reality))
            # print('断言失败信息：' + str(e))
            return False
