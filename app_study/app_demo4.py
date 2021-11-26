# -*- coding: UTF-8 -*-
# 高级手势
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

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
    'appPackage': 'com.android.settings',  # app包名
    # 应用名(包名后面的就是页面名)当前窗口的包名  adb shell dumpsys window | findstr mCurrentFocus
    'appActivity': 'com.android.settings.ChooseLockPattern',
    'noReset': True  # 不重置True不重置，False重置
}
# 启动程序Remote(appium服务器，手机配置信息)wb=webdriver hub=selenium中的一个节点
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
driver.implicitly_wait(10)
# 对蓝牙定位
# blue = driver.find_element('xpath', '//*[@text="蓝牙"]')
# 实例化TouchAction
touch = TouchAction(driver)
# 放入执行的元素，轻敲事件
# touch.tap(blue)
# touch.tap(x=542, y=981)
# 调用执行方法
# touch.perform()
# 按下和抬起   .press()按下    release()抬起
# touch.press(x=542, y=981).release().perform()
# 加入等待时间，1秒后抬起
# touch.press(x=542, y=981).wait(1000).release().perform()

# 移动move_to()
touch.press(x=211, y=900).wait(1000).move_to(x=865, y=900).\
    wait(1000).move_to(x=865, y=1561).release().perform()
sleep(3)
driver.quit()
