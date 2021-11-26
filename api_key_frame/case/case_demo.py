# -*- coding: UTF-8 -*-
import unittest
from ddt import ddt, file_data

from api_key_frame.api_keyword.api_key import ApiKey


@ddt
class ApiCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak = ApiKey()

    @file_data('../data/user.yaml')
    def test_1(self, username, password):
        url = 'http://39.98.138.157:5000/api/login'
        data = {'username': username,
                'password': password
                }
        res = self.ak.do_post(url=url, json=data)
        print(res.text)
        # self.assertEqual(res.status_code, 200, msg='请求错误')

        # 获取响应中的结果用于校验是否成功，传入json()格式返回值，和json内容中的key值
        name = self.ak.get_text(res.text, 'name')
        print(name)
        self.assertEqual(name, 'admin', msg='异常')

        # print(name)
        # self.assertTrue(name)


if __name__ == '__main__':
    unittest.main()
