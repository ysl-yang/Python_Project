# -*- coding: UTF-8 -*-
import requests
from requests import session

url = 'http://39.98.138.157:5000/api/login'
data = {"password": "123456", "username": "admin"}
res = requests.post(url=url, json=data)
# print(res.text)
headers = {
    "token": res.json()['token']
    # "token": "admin"
}

url = 'http://39.98.138.157:5000/api/getuserinfo'
res_get = requests.get(url=url, headers=headers)
print(res_get.text)

# 基于session来实现接口关联的方案：session的创建意味着，基于这个session所产生的相关session信息都会被应用
session = requests.session()
session.get()
session.post()
