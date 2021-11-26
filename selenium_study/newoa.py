# coding = UTF-8
import HTMLTestRunner
import unittest
import warnings
import time
from time import sleep

from selenium import webdriver


class TestCase(unittest.TestCase):
    def setUp(self):
        print('测试用例开始执行')
        warnings.simplefilter('ignore', ResourceWarning)
        # 启动浏览器驱动
        self.driver = webdriver.Edge()
        # 访问的URL
        self.driver.get('http://testnewoa.372163.com/')
        # 浏览器窗口最大户
        self.driver.maximize_window()

    def test_1(self):
        # 定位用户名输入框输入用户名
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('xielulu@372163.com')
        # 定位密码输入框输入密码
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('asdj123')
        # 定位登录按钮点击登录
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
        # 获取当前窗口句柄
        self.driver.current_window_handle
        sleep(5)
        # 截取当前页面图片,time是获取main中的时间变量
        try:
            self.driver.get_screenshot_as_file('D:\\Project\\imgs\\' + time + '.png')
            print('截图成功')
        except BaseException as msg:
            print(msg)
        # 定位登录人的名字
        name = self.driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]').text
        self.assertEqual(name, '谢露露')

    def test_2(self):
        # 定位用户名输入框输入用户名
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('lidanyang@372163.com')
        # 定位密码输入框输入密码
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('asdj123')
        # 定位登录按钮点击登录
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
        # 获取当前窗口句柄
        self.driver.current_window_handle
        sleep(5)
        # 定位登录人的名字
        name = self.driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]').text
        self.assertEqual(name, '谢露露')

    def tearDown(self):
        print('测试用例执行结束')
        # 关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    # 1、通过TestSuite创建一个容器来存储
    suite = unittest.TestSuite()
    # 2、将用例添加到容器
    cases = [TestCase('test_1'), TestCase('test_2')]
    suite.addTests(cases)
    # 或用这种方式添加
    # suite.addTest(TestCase('test_1'))
    # suite.addTest(TestCase('test_2'))
    # 3、获取当前时间用来命名报告
    time = time.strftime('%Y%m%d%H%M%S')
    # 4、通过open方法创建或打开要保存报告的路径及名字
    report = open('D:\\Project\\report\\测试报告' + time + ".html", 'wb')
    # 5、通过HTMLTestRunner内置方法运行生成报告,stream = 存放路径
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=u'测试报告', description=u'测试用例执行情况：')
    # 6、run方法执行容器
    runner.run(suite)
    # 7、关闭写入文件的入口
    report.close()
