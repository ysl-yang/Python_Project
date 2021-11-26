import time

from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.get('http://testnewoa.372163.com/')
sleep(3)
time = time.strftime('%Y%m%d%H%M%S')
print(time)
# 用户名输入框
driver.find_element_by_xpath('//*[@id="username"]').send_keys('xielulu@372163.com')
# 密码输入框
driver.find_element_by_xpath('//*[@id="password"]').send_keys('asdj123')
# 登录输入框
driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
sleep(5)
# 获取当前窗口句柄
driver.current_window_handle
name = driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]')
print(name.text)
# 隐式等待，10秒
sleep(5)
driver.quit()
