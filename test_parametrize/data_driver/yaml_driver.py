# -*- coding: UTF-8 -*-
import yaml


def load_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data

# print(load_yaml())
