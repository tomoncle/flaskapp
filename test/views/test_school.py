#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-15 下午2:01
# @Author         : Tom.Lee
# @File           : test_school.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


import requests


class TestSchool(object):
    def __init__(self):
        self.url = 'http://127.0.0.1:5000/api/schools/'
        self.create()
        # self.update()
        # self.delete()

    def create(self):
        print 'create-' * 10
        print requests.post(
            url=self.url,
            data={'name': '山东政法大学', 'address': 'ShanDong　Jinan'}
        ).text

    def update(self):
        print 'update-' * 10
        print requests.put(
            url=self.url,
            data={'id': 10, 'name': '上海财经大学', 'address': 'ShangHai PuXi'}
        ).text

    def delete(self):
        print 'delete-'*10
        print requests.delete(self.url+'9').text

TestSchool()
