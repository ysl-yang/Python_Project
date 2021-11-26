import unittest
from web_keys_un import WebKeys


class UnitTest(unittest.TestCase):
    # 前置类,前置类只会执行一次，所以就可以实现使用一个浏览器执行多次用例
    @classmethod
    def setUpClass(cls) -> None:
        cls.wk = WebKeys()

    # 后置类
    @classmethod
    def tearDownClass(cls) -> None:
        cls.wk.quit()

    # 前置
    def setUp(self):
        pass
        # self.wk = WebKeys()

    # 后置
    def tearDown(self):
        pass
        # self.wk.quit()

    def test_01(self):
        self.wk.url('https://www.baidu.com/')
        self.wk.input('id', 'kw', '手机')
        self.wk.click('id', 'su')
        self.wk.sleep(2)

    def test_02(self):
        self.wk.url('https://www.baidu.com/')
        self.wk.input('id', 'kw', '电脑')
        self.wk.click('id', 'su')
        self.wk.sleep(2)


if __name__ == '__main__':
    unittest.main()
