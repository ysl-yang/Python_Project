from shop import WebShop
wk = WebShop()
wk.max_win()
wk.url('http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html')
wk.input('name', 'accounts', 'yangshulin')
wk.input('name', 'pwd', '123456')
wk.click('xpath', '//button[@class="am-btn am-btn-primary am-radius am-btn-sm btn-loading-example"]')
wk.sleep(3)
wk.quit()