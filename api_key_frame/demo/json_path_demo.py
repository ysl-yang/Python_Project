# -*- coding: UTF-8 -*-
'''
    JsonPath模块：专门用于处理json字符串的模块
    返回的是list，可能是一个值或多个值存在
    jsonpath要么返回false，要么返回list
'''
import jsonpath

data = {
    "win": [
        {
            "city": "北京",
            "cityid": "101250101",
            "country": "中国",
            "countryEn": "China",
            "orderby": 1
        },
        {
            "city": "上海",
            "cityid": "101250102",
            "country": "中国",
            "countryEn": "China",
            "orderby": 2
        },
        {
            "city": "邢台",
            "cityid": "101250103",
            "country": "中国",
            "countryEn": "China",
            "orderby": 11
        },
        {
            "city": "石家庄",
            "cityid": "101250104",
            "country": "中国",
            "countryEn": "China",
            "orderby": 12
        }
    ]
}
'''
    jsonpath基本表达式
    $   表示根节点
    .   表示或得子节点
    ..  获取所有符合条件的内容
    *   表示所有的元素节点
    []  迭代器的标识，用于处理下标，也就是存放下标
    [,] 中间用逗号隔开可以获取多个指定的元素[0,2]
    ?() 过滤条件固定写法
    @   当前节点
'''
# 基于jsonpath获取元素：通过jsonpath函数来进行获取(json数据，定位表达式)
# rr = jsonpath.jsonpath(data, '$..day')
# 因为默认是list，可以通过打印角标来实现取值
# print(rr[0])
orderby_ = jsonpath.jsonpath(data, '$.win[?(@.orderby>10)]')
print(orderby_)
