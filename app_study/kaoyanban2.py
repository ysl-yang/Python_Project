# -*- coding: UTF-8 -*-
# 高级手势
from time import sleep

import contexts as contexts
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions import context

'''
    1.创建一个touchAction对象
    2.对象调用我们想要做的操作
    3.通过perform()执行
'''
# 参数信息
info = {
    'platformName': 'Android',  # 操作平台
    'platformVersion': '7.1.2',  # 设备版本号
    'deviceName': '127.0.0.1:62001',  # 设备名，取的模拟器（adb devices）
    'appPackage': 'com.tal.kaoyan',  # app包名
    # 应用名(包名后面的就是页面名)当前窗口的包名  adb shell dumpsys window | findstr mCurrentFocus
    'appActivity': 'com.tal.kaoyan.ui.activity.HomeTabActivity',
    'noReset': True  # 不重置True不重置，False重置
}
# 启动程序Remote(appium服务器，手机配置信息)wb=webdriver hub=selenium中的一个节点
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
driver.implicitly_wait(10)


def size():
    # 获取屏幕分辨率
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    return width, height


def swipe_left():
    size2 = size()
    x1 = size2[0] * 0.8
    y1 = size2[1] * 0.9
    x2 = size2[0] * 0.2
    driver.swipe(x1, y1, x2, y1)


touch = TouchAction(driver)
# touch.press(x=960, y=1187).wait(1000).move_to(x=127, y=1187).release().perform()
# 从下往上滑
# touch.press(x=538, y=1252).wait(5000).move_to(x=538, y=558).release().perform()
# driver.switch_to.context("NATIVE_APP")
# driver.switch_to.context("WEBVIEW_1")
sleep(5)
driver.swipe(538, 1252, 538, 558)

# swipe_left()
sleep(5)
# touch = TouchAction(driver)
driver.quit()
