# -*- coding: UTF-8 -*-
'''
    接口测试的操作核心
    1. 准备数据
    2. 发送请求
    3. 判断响应
'''
import unittest
import requests
from ddt import ddt, file_data
from interface_frame.api_key.api_key import ApiKey
from interface_frame.conf import read_ini


@ddt
class CaseDemo(unittest.TestCase):
    # 关联数据赋值行为
    def assignment(self, kwargs):
        for key, value in kwargs.items():
            # 基于数据内容的格式来进行判断该用哪种方式处理
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    # 通过反射将值返回给key
                    kwargs[key] = getattr(self, key)
        return kwargs

    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKey()
        cls.url = read_ini.ReadIni('../conf/config.ini', 'TEST_SERVER', 'url')
        cls.token = None
        cls.userid = None
        cls.openid = None
        cls.cartid = None

    # 登录测试用例定义
    @file_data('../data/user.yaml')
    def test_1(self, path, data):
        # url = self.url + '/api/login'
        url = self.url + path
        res = self.ak.do_post(url=url, json=data)
        # print(res.text)
        # 赋值全局变量，通过类名.变量名来修改当前方法的变量为全局变量
        # CaseDemo.token = self.ak.get_text(res.text, 'token')
        token = self.ak.get_text(res.text, 'token')
        if token:
            CaseDemo.token = token
        # print(self.token)

    # getuserinfo电商获取个人信息接口
    @file_data('../data/userinfo.yaml')
    def test_2(self, path, headers):
        url = self.url + path
        headers['token'] = self.token
        res = self.ak.do_get(url=url, headers=headers)
        # print(res.text)
        userid = self.ak.get_text(res.text, 'userid')
        openid = self.ak.get_text(res.text, 'openid')
        if userid:
            CaseDemo.userid = userid
        if openid:
            CaseDemo.openid = openid
        # print(userid, openid)

    # 添加购物车
    @file_data('../data/addcart.yaml')
    def test_3(self, path, headers, data):
        url = self.url + path
        headers['token'] = self.token
        data['openid'] = self.openid
        data['userid'] = self.userid
        res = self.ak.do_post(url=url, headers=headers, json=data)
        # print(res.text)
        cartid = self.ak.get_text(res.text, 'cartid')
        if cartid:
            CaseDemo.cartid = cartid

    # createorder创建订单接口
    # @file_data('../data/createorder.yaml')
    # def test_4(self, path, headers, data):
    #     url = self.url + path
    #     headers['token'] = self.token
    #     data['openid'] = self.openid
    #     data['userid'] = self.userid
    #     data['cartid'] = self.cartid
    #     res = self.ak.do_post(url=url, headers=headers, json=data)
    #     print(res.text)

    # 关联数据赋值行为，来执行
    @file_data('../data/createorder.yaml')
    def test_4(self, path, **kwargs):
        url = self.url + path
        value = self.assignment(kwargs)
        res = self.ak.do_post(url=url, headers=value['headers'], json=value['data'])
        print(res.text)


if __name__ == '__main__':
    unittest.main()
