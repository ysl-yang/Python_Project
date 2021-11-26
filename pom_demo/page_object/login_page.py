'''
    loginpage：只为系统登录业务而生成的页面对象
'''
from selenium import webdriver
from pom_demo.base_page.base_page import BasePage


# 登录页


# 继承BasePage类来继承封装好的定位、输入等方法
class LoginPage(BasePage):
    '''
        页面对象类的模板
        1.url
        2.关键元素
        3.行为
    '''
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'
    # 关键元素,用元组来存放
    username = ('name', 'accounts')
    password = ('name', 'pwd')
    login_button = ('xpath', '//button[text()="登录"]')

    # 页面业务
    def login(self, user, pwd):
        # 访问登录页，确保能正常登录
        self.visit(self.url)
        # 输入用户名密码
        self.input(self.username, user)
        self.input(self.password, pwd)
        # 点击登录按钮实现登录
        self.click(self.login_button)


# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = 'yangshulin'
    pwd = '123456'
    lp = LoginPage(driver)
    lp.login(user, pwd)
