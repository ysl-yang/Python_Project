'''
    CartPage:校验购物车添加是否成功
'''
from pom_demo.base_page.base_page import BasePage


class CartPage(BasePage):
    # url
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/cart/index.html'

    goods = ('xpath', '//a[contains(text(),"苹果")]')

    # 校验商品是否存在
    def cart_info(self):
        self.visit(self.url)
        self.get_text(self.goods)
