# -*- coding: UTF-8 -*-
# 高级手势
from time import sleep

from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

'''
    1.创建两个手指，创建2个TouchAction对象
    2.创建mulitAction()对象
    3.把2个TouchAction对象添加到mulitAction()
    3.通过perform()执行
'''
# 参数信息
info = {
    'platformName': 'Android',  # 操作平台
    'platformVersion': '7.1.2',  # 设备版本号
    'deviceName': 'baidu',  # 设备名，取的模拟器（adb devices）
    'appPackage': 'com.baidu.BaiduMap',  # app包名
    # 应用名(包名后面的就是页面名)当前窗口的包名  adb shell dumpsys window | findstr mCurrentFocus
    'appActivity': 'com.baidu.baidumaps.MapsActivity',
    'noReset': True  # 不重置True不重置，False重置
}
# 启动程序Remote(appium服务器，手机配置信息)wb=webdriver hub=selenium中的一个节点
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
driver.implicitly_wait(10)
# 1.获取屏幕尺寸
width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
print(width, height)
sleep(10)
# 2.放大、缩小地图
touch1 = TouchAction(driver)
touch1.press(x=width * 0.2, y=height * 0.2).wait(1000).move_to(x=width * 0.4, y=height * 0.6).wait(1000).release()

touch2 = TouchAction(driver)
touch1.press(x=width * 0.8, y=height * 0.8).wait(1000).move_to(x=width * 0.5, y=height * 0.5).wait(1000).release()
print(width * 0.2)
print('执行缩小操作')
# 实例化MultiAction
mu = MultiAction(driver)
# 添加动作
mu.add(touch1, touch2)
# 执行
mu.perform()
# 进入h5页面，要先进入contextts
contexts = driver.contexts
print(contexts)
# 切换到h5页面，将contexts传入
driver.switch_to.context('WEBVIEW_com.tencent.edu')
# 退回至原生
driver.switch_to.context('NATIVE_APP')
sleep(10)
driver.quit()
