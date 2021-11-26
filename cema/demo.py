from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://music.163.com/')
driver.find_element('link text', '登录').click()
driver.find_element('link text', '选择其他登录模式').click()
driver.find_element('xpath', '//input[@id="j-official-terms"]').click()
driver.find_element('link text', 'QQ登录').click()
sleep(3)
dd = driver.current_window_handle
print(dd)
# ha = driver.window_handles
# driver.switch_to.window(ha[1])
# print(driver.title)
driver.quit()
