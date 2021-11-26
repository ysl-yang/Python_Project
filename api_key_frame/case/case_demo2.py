# -*- coding: UTF-8 -*-
import unittest
import requests

from ddt import ddt, file_data


@ddt
class ApiUnit(unittest.TestCase):

    @file_data('../data/user.yaml')
    def test_1(self, username, password):
        url = 'http://39.98.138.157:5000/api/login'
        data = {'username': username,
                'password': password
                }
        res = requests.post(url=url, data=data)
        res.json()


if __name__ == '__main__':
    unittest.main()
