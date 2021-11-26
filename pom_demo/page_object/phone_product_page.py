'''
    手机商品详情页：PhonePage，主要显示手机的商品详情内容，用于执行对应的操作行为
'''
from selenium import webdriver
from pom_demo.base_page.base_page import BasePage


# 登录页


# 继承BasePage类来继承封装好的定位、输入等方法
class PhonePage(BasePage):
    '''
        页面对象类的模板
        1.url
        2.关键元素
        3.行为
    '''
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html'
    # 关键元素,用元组来存放
    suite = ('xpath', '//li[@data-value="套餐一"]')
    color = ('xpath', '//li[@data-value="金色"]')
    memory = ('xpath', '//li[@data-value="32G"]')
    add_cart_button = ('xpath', '//button[text()="加入购物车"]')

    # 添加购物车行为
    def add_cart(self):
        # 访问页面
        self.visit(self.url)
        # 选择商品属性
        self.click(self.suite)
        self.wait(1)
        self.click(self.color)
        self.wait(1)
        self.click(self.memory)
        # 点击添加购物车
        self.click(self.add_cart_button)


# 调试
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     pp = PhonePage(driver)
#     pp.add_cart()
