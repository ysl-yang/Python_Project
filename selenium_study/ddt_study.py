import warnings
from ddt import ddt, data, unpack
import unittest
from selenium import webdriver
import time

testData = (["selenium", "pytest"], ["python", "yield "])  # 多个参数


@ddt
class testDDT(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com/')

    # 把数据改成变量存储运行时，需要在前面加*
    @data(*testData)
    @unpack
    def testddt(self, data1, data2):
        self.driver.find_element_by_css_selector('#kw').send_keys(data1, data2)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#su').click()

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
