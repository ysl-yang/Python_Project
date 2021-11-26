# -*- coding: UTF-8 -*-
import requests
import json

url = 'https://openapiv53.ketangpai.com//UserApi/login'
data = {"email": "2331232525@qq.com", "password": "ysl19960219YSL", "remember": "0"}
# 发起post请求
r = requests.post(url, json=data)
# 响应状态码
# print(r.status_code)
# 响应头
# print(r.headers)
# 响应体-字典类型
print(r.json())
print('=' * 30)
print('响应cookies:', r.cookies)
