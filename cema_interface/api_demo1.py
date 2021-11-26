# -*- coding: UTF-8 -*-


import requests
import json
# 接口请求数据模拟
# 数据的生成
from cema_interface import api_demo2

data = {
    "username": "admin",
    "password": api_demo2.hashmd5("123456")
}
headers = {"Content-Type": "application/json"}
# 将data转换为json对象：通过使用json库来进行转换
jsondata = json.dumps(data)
print(jsondata)

# 接口的地址
url = 'http://39.98.138.157:5000/api/login'
# 将数据传递到对应的接口地址，来实现一次该接口的请求下发，定义对应的请求方式
res = requests.post(url=url, data=jsondata, headers=headers)
# 响应代码
# print(res.status_code)
# 原始内容
# print(res.content)
# 文本内容,编译后的内容
print(res.text)
# 请求头
# print(res.request.headers)
# 将数据进行转码，从json转换为字典
content = json.loads(res.text)
# assert 'success' == content['msg']
