# -*- coding: UTF-8 -*-
import requests

# url = 'http://39.98.138.157:5000/api/login'
# data = {"username": "admin", "password": "123456"}
# res = requests.post(url=url, json=data)
# print(res.text)

url = 'http://39.98.138.157:5000/api/getuserinfo'
headers = {"token": "23657DGYUSGD126731638712GE18271H"}
res = requests.get(url=url, headers=headers)
print(res.text)
