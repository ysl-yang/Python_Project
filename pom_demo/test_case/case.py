'''
    测试用例类，所有的测试代码都在这里实现
'''
import unittest
from selenium import webdriver
from ddt import ddt, file_data
from pom_demo.page_object.cart_page import CartPage
from pom_demo.page_object.login_page import LoginPage
from pom_demo.page_object.phone_product_page import PhonePage


@ddt
class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        # 实例化三个page页，将driver传入用来确保使用的使用一个浏览器
        cls.lp = LoginPage(cls.driver)
        cls.pp = PhonePage(cls.driver)
        cls.cp = CartPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登录
    @file_data('../data/users.yaml')
    def test_01_login(self, user, pwd):
        # users = 'yangshulin'
        # pwds = '123456'
        # 调用lp的login方法，传入用户名密码
        self.lp.login(user, pwd)

    # 添加购物车
    def test_02_add_cart(self):
        # 调用pp添加购物车方法
        self.pp.add_cart()

    # 检查购物车
    def test_03_ex_cart(self):
        # 调用cp校验购物车
        self.cp.cart_info()


'''
    def test_shopxo(self):
        driver = webdriver.Chrome()
        # 实例化三个page页，将driver传入用来确保使用的使用一个浏览器
        lp = LoginPage(driver)
        pp = PhonePage(driver)
        cp = CartPage(driver)
        # 定义用户名、密码
        users = 'yangshulin'
        pwds = '123456'
        # 调用lp的login方法，传入用户名密码
        lp.login(users, pwds)
        # 调用pp添加购物车方法
        pp.add_cart()
        # 调用cp校验购物车
        cp.cart_info()
'''

if __name__ == '__main__':
    unittest.main()
