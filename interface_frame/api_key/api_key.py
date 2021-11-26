# -*- coding: UTF-8 -*-
'''
    这是接口关键字驱动类，用于提供自动化接口测试的关键字方法
    主要实现常用的关键字内容，并定义好所有的参数的内容即可
    接口中的常用关键字：post\get\put\delete\header....
    关键字驱动模式下的分层处理
    1.配置有关键字的模块
    2.用例模块
    3.数据模块
    4.配置模块
    5.日志模块
    6.测试报告、套件
'''
import json

import requests
import jsonpath


class ApiKey:
    # get请求的封装,使用**kwargs时要加return（代表使用get下所有的方法）
    # 因为params存在空值情况,存放默认值None
    def do_get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    def do_post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    # 基于jsonpath获取数据的关键字,用于提取所需要的内容
    def get_text(self, txt, key):
        try:
            # jsonpath获取数据的表达式：成功返回list，失败返回false
            txt = json.loads(txt)
            value = jsonpath.jsonpath(txt, '$..{0}'.format(key))
            if value:
                if len(value) == 1:
                    return value[0]
                return value
        except Exception as e:
            return e
        return value


# if __name__ == '__main__':
#     ak = ApiKey()
#     data = {'username': 'admin',
#             'password': '123456'}
#     res = ak.do_post(url='http://39.98.138.157:5000/api/login', json=data)
#     print(res.text)
