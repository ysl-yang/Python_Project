'''
    基类：pom体系下的底层代码，用于封装各类行为操作，便于页面对象类进行调用
        根本核心是关键字驱动设计理念
'''
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 创建临时driver
    # driver = webdriver.Chrome()

    # 构造函数
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 定位元素
    def locate(self, loc):
        return self.driver.find_element(*loc)

    # 点击操作
    def click(self, loc):
        self.locate(loc).click()

    # 输入
    def input(self, loc, txt):
        self.locate(loc).send_keys(txt)

    # 句柄切换，传入角标切换句柄
    def switch_handle(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    # 句柄的切换（考虑不同场景的不同切换）
    def switch_handle_1(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # iframe切换default窗体
    def switch_default(self):
        self.driver.switch_to.default_content()

    # 断言文本信息：可以捕获异常进行处理，也可以不捕获，因为报错就相当于断言失败。
    def assert_text(self, loc, expect):
        try:
            reality = self.locate(loc).text
            assert expect == reality, '断言失败，实际结果为：{}'.format(reality)
            return True
        except Exception as e:
            print('断言失败信息：' + str(e))
            return False

    # 获取指定元素的文本
    def get_text(self, loc):
        return self.locate(loc).text

    # 退出
    def quit(self):
        self.driver.quit()

    # 显式等待
    def web_el_wait(self, loc):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.locate(loc), message='元素查找失败')

    # 强制等待
    def wait(self, time_):
        sleep(int(time_))
