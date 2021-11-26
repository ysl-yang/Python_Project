# _*_ coding:UTF-8
import os.path
import time
import unittest
import warnings
from selenium import webdriver
from time import sleep
import HTMLTestRunner
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('开始执行用例：')
        # 启动浏览器
        self.driver = webdriver.Edge()
        # 窗口最大化
        self.driver.maximize_window()
        # 访问URL
        self.driver.get('http://testnewoa.372163.com/')

    def test_1(self):
        # 用户名输入框
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('xielulu@372163.com')
        # 密码输入框
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('asdj123')
        # 登录输入框
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
        # 强制等待5秒
        sleep(5)
        # 获取当前句柄
        self.driver.current_window_handle
        # 获取用户名
        name = self.driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]').text
        self.assertEqual(name, '谢露露')

    def test_2(self):
        # 用户名输入框
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('lidanyang@372163.com')
        # 密码输入框
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('asdj123')
        # 登录输入框
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
        # 隐式等待，10秒
        self.driver.implicitly_wait(100)
        # 获取当前句柄
        self.driver.current_window_handle
        # 获取用户名
        name = self.driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]').text
        self.assertEqual(name, '谢露露')

    def test_3(self):
        # 用户名输入框
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('lidanyang01@372163.com')
        # 密码输入框
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('asdj123')
        # 登录输入框
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
        # 隐式等待，10秒
        self.driver.implicitly_wait(100)

    def tearDown(self):
        print('执行用例结束')
        self.driver.quit()


if __name__ == '__main__':
    # 1、定义一个测试容器
    Result = unittest.TestSuite()
    # 2、TestCase是类名  将该类下的测试用例加入到测试容器中
    cases = [TestCase("test_1"), TestCase("test_2"), TestCase("test_3")]
    Result.addTests(cases)
    # Result.addTest(TestCase("test_1"))
    # Result.addTest(TestCase("test_2"))
    # Result.addTest(TestCase("test_3"))
    # 3、获取当前时间，用来命名测试报告
    time = time.strftime('%Y%m%d%H%M%S')
    # 4、打开一个文件，将result写入此file中
    fp = open('D:\\Project\\report\\测试报告' + time + ".html", 'wb')
    # 5、stream要写入文件的路径
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况：")
    # 6、运行测试容器
    runner.run(Result)
    fp.close()
