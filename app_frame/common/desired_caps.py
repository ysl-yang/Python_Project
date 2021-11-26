# -*- coding: UTF-8 -*-
import yaml
from appium import webdriver

'''
    启动配置信息
'''


# 去读yaml文件
def appium_desired():
    with open('../config/desired_caps.yaml', 'r', encoding='utf-8') as f:
        # 取yaml文件
        data = yaml.load(f, yaml.FullLoader)
        # print(data)
    # 拿到数据之后，放在配置参数里面
    info = {}
    info['platformName'] = data['platformName']
    info['platformVersion'] = data['platformVersion']
    info['deviceName'] = data['deviceName']
    info['appPackage'] = data['appPackage']
    info['appActivity'] = data['appActivity']
    info['noReset'] = data['noReset']
    # print(info)
    # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
    driver = webdriver.Remote('http://' + data['ip'] + ':' + data['port'] + '/wd/hub', info)
    driver.implicitly_wait(8)
    return driver
