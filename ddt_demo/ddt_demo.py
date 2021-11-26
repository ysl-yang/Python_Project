import unittest

from ddt import ddt, data, unpack, file_data

from web_keys_ddt import WebKeys

'''
    安装 pip install ddt_demo
    导包 from ddt_demo import ddt_demo
    ddt模块所有的内容都是基于装饰器的形式来实现补充的
    也就是在class前假如@ddt_demo，来声明ddt的调用，在需要调用数据驱动的用例前，调用@data，实现数据的驱动分离
'''


# 通过文件读取
def read_file():
    li = []
    file = open('./data.txt', 'r', encoding='utf-8')
    for line in file.readlines():
        li.append(line)
    return li


@ddt  # 表示现在开始，这个测试用例类要调用ddt模块实现数据驱动
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

    '''
        当需要传入多个参数时需要通过unpack将data的数据按顺序拆包，按顺序传入
    '''

    # @data(('https://www.baidu.com/', '手机'))
    # @data(['https://www.baidu.com/', '手机'])   # 列表
    # @data({'https://www.baidu.com/', '手机'})   # 字典
    # @unpack
    # def test_01(self, url, name):
    #     self.wk.url(url)
    #     self.wk.input('id', 'kw', name)
    #     self.wk.click('id', 'su')
    #     self.wk.sleep(2)

    # 基于文件读取，加星的目的是为了拆
    # @data(*read_file())
    @file_data('./data.yaml')
    def test_02(self, **kwargs):
        self.wk.url(kwargs['url'])
        self.wk.input(**kwargs['input'])
        self.wk.click(**kwargs['click'])
        self.wk.sleep(2)


if __name__ == '__main__':
    unittest.main()
