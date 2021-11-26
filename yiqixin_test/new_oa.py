import HTMLTestRunner
import time
import unittest
import warnings
from time import sleep
from ddt_yaml import ddt, data, unpack

from selenium import webdriver


@ddt
class TestCase(unittest.TestCase):
    r_data = [{"user": "xielulu@372163.com", "pwd": "asdj123"},
              {"user": "lidanyang@372163.com", "pwd": "asdj123"}]

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('用例执行开始')
        # 启动浏览器驱动
        self.driver = webdriver.Edge()
        # 打开url
        self.driver.get('http://testnewoa.372163.com/')
        # 窗口最大化
        self.driver.maximize_window()
        # ddt存储username和password

    @data(*r_data)
    def test_1(self, user_data):
        # 定位用户名输入框并输入内容
        self.driver.find_element_by_id('username').send_keys(user_data["user"])
        # 定位密码输入框并输入密码
        self.driver.find_element_by_id('password').send_keys(user_data["pwd"])
        # 定位登录按钮并点击登录
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
        sleep(5)
        # 获取登录页面后的句柄
        self.driver.current_window_handle
        # 获取登录用户名
        name = self.driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]').text
        # 截取当前页面
        try:
            self.driver.get_screenshot_as_file('D:\\Project\\imgs\\' + time + '.png')
            print('截图成功')
        except BaseException as msg:
            print(msg)
        # 对比数据
        self.assertEqual('谢露露', name)

    """
    def test_2(self):
        # 定位用户名输入框并输入内容
        self.driver.find_element_by_id('username').send_keys('lidanyang@372163.com')
        # 定位密码输入框并输入密码
        self.driver.find_element_by_id('password').send_keys('asdj123')
        # 定位登录按钮并点击登录
        self.driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
        sleep(3)
        # 获取登录页面后的句柄
        self.driver.current_window_handle
        # 获取登录用户名
        name = self.driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]').text
        # 对比数据
        self.assertEqual('谢露露', name)
    """

    def tearDown(self):
        print('用例执行结束')
        self.driver.quit()


if __name__ == '__main__':
    # 创建存储容器
    suite = unittest.TestSuite()
    # 将用例添加到容器中
    suite.addTest(TestCase('test_1_1'))
    suite.addTest(TestCase('test_1_2'))
    # suite.addTest(TestCase('test_2'))
    # 生成当前时间
    time = time.strftime('%Y%m%d%H%M%S')
    # 生成测试报告的路径
    result = open('D:\\Project\\report\\测试报告' + time + '.html', 'wb')
    # 添通过测试模板生成测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=result, title='测试报告', description='测试详情：')
    # runner运行run方法执行suite套件
    runner.run(suite)
    # 关闭写入文件入口
    result.close()
