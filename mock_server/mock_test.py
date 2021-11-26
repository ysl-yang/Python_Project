# -*- coding: UTF-8 -*-
import unittest
from unittest import mock

import requests

from mock_server import mock_server_demo1
from mock_server_demo1 import login


class Demo(unittest.TestCase):
    # 基于装饰器的形态来实现的mock，定义哪个接口需要mock
    @mock.patch('mock_server_demo1.login')
    def test_1(self, mock_login):
        # 通过return_value将值返回给login方法,mock的操作相当于自主定义生成测试数据，快速提供至测试行为之中
        a = mock_login.return_value = {"username": "admin",
                                       "password": "123456"}
        # print(a)
        res = requests.post(url='http://39.98.138.157:5000/api/login', json=a)
        print(res.text)

    # mock实现形式，如果实现多次调用，每次使用不同的值
    @mock.patch.object(mock_server_demo1,'sum')
    def test_2(self,mock_login):
        mock_login.side_effect={
            'login1',
            'login2',
            'login3',
        }


if __name__ == '__main__':
    unittest.main()
