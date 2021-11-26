import threading

from selenium import webdriver


def open(driver):
    driver.get('https://www.baidu.com/')
    driver.quit()


open(webdriver.Chrome())

th = []
dri1 = webdriver.Chrome()
dri2 = webdriver.Chrome()
dri3 = webdriver.Chrome()
# 添加线程target=存放的方法
th.append(threading.Thread(target=open, args=[dri1]))
th.append(threading.Thread(target=open, args=[dri2]))
th.append(threading.Thread(target=open, args=[dri3]))
# 所有线程都需要手动调用，通过start方法
for t in th:
    t.start()
    # 当前线程执行完后再执行下一个线程，就相当于变为了单线程，
    # 用于避免线程死锁，也可以用线程锁来实现
    # t.join()
