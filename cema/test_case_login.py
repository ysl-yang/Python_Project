from web_keys import WebKeys

wk = WebKeys()
wk.max_widonws()
wk.url('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
wk.input('name', 'accounts', 'yangshulin')
wk.input('name', 'pwd', '123456')
wk.click('xpath', '//button[@class="am-btn am-btn-primary am-radius am-btn-sm btn-loading-example"]')
wk.click('link text', '首页')
wk.click('xpath', '//*[@id="floor1"]/div[2]/div[2]/div[1]/a')
wk.sleep(3)
wk.switch_handle_1(0)
wk.sleep(3)
wk.quit()
