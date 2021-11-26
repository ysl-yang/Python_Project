# -*- coding: UTF-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

'''
qwerty2664
qwerty123
建立连接adb connect 127.0.0.1:62001（夜神模拟器的端口号）
检测adb devices
进入手机内部adb shell
安装文件，adb install “拖动apk到cmd”
覆盖安装，adb install -r “拖动apk到cmd”
查找包名aapt dump badging “拖动apk到cmd”
查找包名adb shell pm list packages
卸载 adb uninstall 包名
输出日志 adb logcat>d:\log.txt
输出日志及时间 adb logcat -v time>d:\log.txt
电脑文件传输到手机 adb push “电脑存放位置”  “手机文件位置”
手机文件传输到电脑 adb pull “手机文件位置”  “电脑存放位置”
手机截屏 adb shell screencap “手机文件位置”
当前窗口的包名  adb shell dumpsys window | findstr mCurrentFocus

adb shell monkey --pct-touch 100（指的100%）
1.触摸事件 --pct-touch
2.手势事件 --pct-motion
3.二指缩放事件 --pct-pinchzoom
4.轨迹事件 --pct-trackball
5.屏幕旋转事件 --pct-rotation
6.基本导航事件 --pct-nav
7.主要导航事件 --pct-majornav
8.系统按键事件 --pct-syskeys
9.app切换事件 --pct-appswitch
10.键盘事件 --pct-flip
其他类型事件 --pct-anyevent
'''
# 参数信息
info = {
    'platformName': 'Android',  # 操作平台
    'platformVersion': '7.1.2',  # 设备版本号
    'deviceName': '127.0.0.1:62001',  # 设备名，取的模拟器（adb devices）
    'appPackage': 'com.android.settings',  # app包名
    # 应用名(包名后面的就是页面名)当前窗口的包名  adb shell dumpsys window | findstr mCurrentFocus
    'appActivity': 'com.android.settings.Settings',
    'noReset': False,  # 不重置true不重置，false重置
    'automationName': 'uiautomator2'
}
# 启动程序Remote(appium服务器，手机配置信息)wb=webdriver hub=selenium中的一个节点
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
# 元素定位 id class xpath，结合\tools\uiautomatorviewer.bat的使用
# driver.implicitly_wait(10)
# sleep(5)
# swipe语法swipe(开始x坐标、开始y坐标、结束x坐标、结束y坐标),设置惯性，单位毫秒，在时间内进行滑动
driver.swipe(538, 1252, 507, 558)
# 老师代码位置
# driver.swipe(535, 1610, 579, 635, 3000)

# touch = TouchAction(driver)
# touch.press(x=538, y=1252).wait(1000).move_to(x=538, y=558).release().perform()

# id = resource-id
# driver.find_element(By.ID, 'com.android.settings:id/search').click()  #点击搜索
# driver.find_element('id', 'com.android.settings:id/search').click()   #点击搜索
# xpath定位
# driver.find_element('xpath', '//*[@content-desc="搜索设置"]').click() #点击搜索
# 只能传content-desc，但这个值不是所有的元素都有
# driver.find_element_by_accessibility_id('搜索设置')
# driver.find_element('id', 'android:id/search_src_text').send_keys('测试')
# driver.find_element('xpath', '//*[@content-desc="收起"]').click()   #返回上一页

# address = driver.find_element(By.XPATH, '//*[@text="位置信息"]')  # 位置信息
# more = driver.find_element(By.XPATH, '//*[@text="更多"]')  # 更多
# scroll滚动：从一个元素滑动到另一个元素
# driver.scroll(address, more)

# drag_and_drop：从一个元素滑动到另一个元素，没有惯性
# driver.drag_and_drop(address, more)

sleep(5)

# 关闭
driver.quit()
