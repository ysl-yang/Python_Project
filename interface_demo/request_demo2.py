# -*- coding: UTF-8 -*-
import requests
import json

url = 'https://openapiv53.ketangpai.com//UserApi/login'
data = {"email": "2331232525@qq.com", "password": "ysl19960219YSL", "remember": "0"}
# 将会话通过.Session()进行存储，后面再调用其他接口时不再需要传cookie
ss = requests.Session()
resp = ss.post(url, data=data)
resp_dict = resp.json()
print(resp_dict)
token = resp_dict['data']['token']  # 获取data下token
print(token)
print('=' * 30)
# url = 'https://openapiv53.ketangpai.com//UserApi/getUserInfo'
# resp2 = ss.get(url)
# print(resp2.json())
