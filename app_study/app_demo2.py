# -*- coding: UTF-8 -*-
'''
    app的应用场景，滑动
    滑动：swipe、scroll、drag_and_drop
'''
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

# 参数信息
info = {
    'platformName': 'Android',  # 操作平台
    'platformVersion': '7.1.2',  # 设备版本号
    'deviceName': '127.0.0.1:62001',  # 设备名，取的模拟器（adb devices）
    'appPackage': 'com.android.settings',  # app包名
    # 应用名(包名后面的就是页面名)当前窗口的包名  adb shell dumpsys window | findstr mCurrentFocus
    'appActivity': 'com.android.settings.Settings',
    'noReset': True  # 不重置true不重置，false重置
}
# 启动程序Remote(appium服务器，手机配置信息)wb=webdriver hub=selenium中的一个节点
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
# size = driver.get_window_size()
driver.implicitly_wait(5)
# sleep(5)
# swipe语法swipe(开始x坐标、开始y坐标、结束x坐标、结束y坐标),设置惯性，单位毫秒，在时间内进行滑动
# driver.swipe(538, 1252, 507, 558)
# 老师代码位置
driver.swipe(535, 1610, 579, 635, 3000)
# driver.swipe(size["width"] * 0.5, size["heigth"] * 0.9, size["width"] * 0.5, size["heigth"] * 0.1)
# scroll 元素滑动，从一个元素滑动到另一个元素
address = driver.find_element(By.XPATH, '//*[@text="位置信息"]')  # 位置信息
more = driver.find_element(By.XPATH, '//*[@text="更多"]')  # 更多
# 传入开始位置，结束位置
driver.scroll(address, more)
# drag_and_drop，从一个元素滑动到另一个元素，没有惯性
driver.drag_and_drop(address, more)

sleep(5)
driver.quit()
