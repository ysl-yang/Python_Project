from time import sleep
from selenium import webdriver
# 启动浏览器驱动
driver = webdriver.Edge()
driver.get('http://testnewoa.372163.com/')
# 窗口最大化
driver.maximize_window()
# 用户名输入框
driver.find_element_by_xpath('//*[@id="username"]').send_keys('lidanyang@372163.com')
# 密码输入框
driver.find_element_by_xpath('//*[@id="password"]').send_keys('asdj123')
# 登录按钮
driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
# 等待10
driver.implicitly_wait(10)
# driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/ul/li[6]/div').click()
# 获取当前句柄
driver.current_window_handle
# 点击更多
driver.find_element_by_xpath('//*[@id="module_1"]/div[1]/a').click()
# driver.find_element_by_link_text('客户管理').click()
sleep(3)
driver.quit()