# -*- coding: UTF-8 -*-
import pytest
import requests

from test_parametrize.data_driver import yaml_driver

token = None
# parametrize的参数要和方法中的参数名对应
# @pytest.mark.parametrize(['username', 'password'], [('admin', '123456'),('admin1', '123456')])
@pytest.mark.parametrize('data', yaml_driver.load_yaml('../data/user.yaml'))
def test_login(data):
    url = 'http://39.98.138.157:5000/api/login'
    res = requests.post(url=url, json=data)
    global token
    token = res.json()['token']
    print(res.text)
    print(token)
    # print(data)


if __name__ == '__main__':
    pytest.main(['-s'])
