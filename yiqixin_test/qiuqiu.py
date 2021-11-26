import random

import pywinauto
from pywinauto.keyboard import send_keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from pywinauto import Application

driver = webdriver.Edge()
driver.get('http://testnewoa.372163.com/')
driver.maximize_window()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
# wait = WebDriverWait(driver,10,0.5)
# wait.until(EC.presence_of_element_located((By.ID, 'username')))
# but = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button/span')))
# print(but)
# driver.quit()

driver.find_element_by_id('username').send_keys('xielulu@372163.com')
driver.find_element_by_id('password').send_keys('Td2021--')
driver.find_element_by_xpath('//*[@id="root"]/section/section[2]/form/div[3]/div/div/span/button').click()
sleep(3)
driver.current_window_handle
user_name = driver.find_element_by_xpath('//*[@id="root"]/section/section/header/div[2]/span[2]')
# 实例化
acc = ActionChains(driver)
# 定义鼠标动作
acc.move_to_element(user_name)
# 执行鼠标
acc.perform()
sleep(3)
driver.find_element_by_xpath('//li[text()="个人信息"]').click()
sleep(3)
up = driver.find_element_by_xpath('//span[@role= "button"]')
acc.click(up)
acc.perform()
# app = pywinauto.Desktop()
# app.top_from_point('C:\\Users\\yang\\Desktop\\业绩')
sleep(5)
send_keys('"C:\\Users\\yang\\Desktop\\业绩\\分成人1.png"')
send_keys('{VK_RETURN}')

sleep(2)
# driver.quit()



# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# x = Person('小米', '大米')
# x.printname()
"""
random_nums_list = []
for i in range(1, 7):
    random_nums_list.append(str(random.randint(1, 33)))
blue = random.randint(1, 16)
print('红球：'+' '.join(random_nums_list)+'\n'+'蓝球：'+str(blue))
"""
