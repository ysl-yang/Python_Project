# -*- coding: UTF-8 -*-
# 读取ini配置文件的模块
import configparser


# 读取配置文件中的内容
def ReadIni(path, selection, option):
    conf = configparser.ConfigParser()
    conf.read(path)
    value = conf.get(selection, option)
    return value
