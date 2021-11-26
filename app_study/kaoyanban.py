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
    'appPackage': 'com.tal.kaoyan',  # app包名
    # 应用名(包名后面的就是页面名)当前窗口的包名  adb shell dumpsys window | findstr mCurrentFocus
    'appActivity': 'com.kaoyan.kylogin.ui.login.LoginKActivity',
    'noReset': True  # 不重置True不重置，False重置
}
# 启动程序Remote(appium服务器，手机配置信息)wb=webdriver hub=selenium中的一个节点
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
driver.implicitly_wait(10)
# touch = TouchAction(driver)
# 关闭弹窗
driver.find_element('id', 'android:id/button1').click()
driver.find_element('id', 'android:id/button1').click()
# 切换密码登录
driver.find_element('id','com.tal.kaoyan:id/loginRegistorcodeAndPassword').click()
# 输入用户名
driver.find_element('id', 'com.tal.kaoyan:id/loginEmailEdittext').send_keys('qwerty2664')
sleep(3)
# 输入密码
driver.find_element('id', 'com.tal.kaoyan:id/loginPasswordEdittext').send_keys('qwerty123')
sleep(3)
# 勾选同意
driver.find_element('id', 'com.tal.kaoyan:id/loginTreatyCheckboxPassword').click()
sleep(3)
# 点击登录
driver.find_element('id', 'com.tal.kaoyan:id/loginLoginBtn').click()
sleep(5)
driver.quit()
