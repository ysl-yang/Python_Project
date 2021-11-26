# -*- coding: UTF-8 -*-
from unittest import result

import openpyxl

# excel测试用例的读取和写入
# class ExcelRead:
from interface_excel.api_key.api_key import ApiKey

excel = openpyxl.load_workbook('../cases/api_cases.xlsx')
sheet = excel['Sheet1']
ak = ApiKey()
# 解决第三方库没有代码提示
assert isinstance(sheet, openpyxl.workbook.workbook.Worksheet)
for value in sheet.values:
    # 准备数据、模拟请求、校验结果
    if type(value[0]) is int:
        # 准备测试数据，地址+路径
        url = value[1] + value[2]
        # 类型转换,eval函数就是实现list、dict、tuple与str之间的转化
        # headers = eval(value[4])  # 请求头
        data = eval(value[5])  # 参数
        # 获取参数类型json\data在以变量的形式传给字典中作为key，当时json就是json，data格式就是data
        data_type = value[6]
        assert_value = value[7]
        # 判断角标4对应列是否有值
        if value[4]:
            # 底层是通过**kwargs来传参，所以这里存放到一个字典中
            dict_data = {
                'url': url,
                'headers': eval(value[4]),
                data_type: data
            }
        else:
            dict_data = {
                'url': url,
                data_type: data
            }
        print(dict_data)
        # 模拟请求，传入字典，让底层代码解析**kwargs
        res = getattr(ak, value[3])(**dict_data)
        # 校验结果
        ak.get_text(res.text, assert_value)
        assert result == value[8], '预期与实际不符合'
        # try:
        #     print(res.json())
        # except:
        #     print(1)
