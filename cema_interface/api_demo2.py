# -*- coding: UTF-8 -*-
import hashlib

# md5加密
arg = '加密前'
se = hashlib.md5(arg.encode('utf-8'))
# 获取内存地址
print(se)
# 获取值
print(se.hexdigest())


# MD5加密函数
def hashmd5(string):
    return hashlib.md5(str(string).encode('utf-8')).hexdigest()
