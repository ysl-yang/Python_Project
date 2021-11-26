# -*- coding: UTF-8 -*-
import requests
import json


class HttpClient(object):
    '''
        通过类名来做实例化
    '''


def __init__(self):
    self.session = requests.session()


def send_request(self, method, url, params_type="from", data=None, **kwargs):
    method = method.upper()
    params_type = params_type.upper()

    # 如果data是字符串，就将字符串转换为字典
    if isinstance(data, str):
        data = json.loads(data)
    if "GET" == method:
        response = self.session.request(method=method, url=url, params=data, **kwargs)
    elif "POST" == method:
        if "FORM" == params_type:  # 发送表单数据，使用data参数传递
            self.session.request(method=method, url=url, data=data, **kwargs)
        else:  # "JSON" == params_type:    #使用json传参
            self.session.request(method=method, url=url, json=data, **kwargs)
    elif "PUT" == method:
        if "FORM" == params_type:  # 发送表单数据，使用data参数传递
            self.session.request(method=method, url=url, data=data, **kwargs)
        else:  # "JSON" == params_type:    #使用json传参
            self.session.request(method=method, url=url, json=data, **kwargs)
    elif "DELETE" == method:
        if "FORM" == params_type:  # 发送表单数据，使用data参数传递
            self.session.request(method=method, url=url, data=data, **kwargs)
        else:  # "JSON" == params_type:    #使用json传参
            self.session.request(method=method, url=url, json=data, **kwargs)
    else:
        raise ValueError('request method"{}" error'.format(method))


def __call__(self, method, url, params_type="form", data=None, **kwargs):
    return self.send_request(method, url, params_type, data, **kwargs)


def close_session(self):
    self.session.close()
