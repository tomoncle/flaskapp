#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-15 上午10:00
# @Author         : Tom.Lee
# @File           : utils.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from .tools import parser_properties


class ParserProperties(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.__file_data = parser_properties(self.file_path)

    @property
    def data(self):
        return self.__file_data

    def get(self, key):
        if key in self.data.keys():
            return self.data[key]
