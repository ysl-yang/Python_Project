'''
    读取yaml
'''
import yaml

file = open('data3.yaml', 'r', encoding='utf-8')
# 读取yaml文件，FullLoader忽略警告
data = yaml.load(stream=file, Loader=yaml.FullLoader)
print(data)