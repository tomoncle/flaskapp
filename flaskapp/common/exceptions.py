#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-4-28 下午3:13
# @Author         : Tom.Lee
# @File           : exceptions.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


class CommonError(Exception):
    code = 500
    error = "CommonError"
    message = "unknown error."

    def __init__(self, code=None, error=None, message=None):
        self.code = self.__class__.code if not code else code
        self.error = self.__class__.error if not error else error
        self.message = self.__class__.message if not message else message

    def __str__(self):
        return '<{}>: {}'.format(self.__class__.__name__, self.message)


class FileNotExistsError(CommonError):
    code = 500
    error = "FileNotExistsError"
    message = "file is not exists."


class JsonEncoderError(CommonError):
    code = 500
    error = "JsonEncoderError"
    message = "json encoder error."


class MySQLDataError(CommonError):
    code = 500
    error = "MySQLDataError"
    message = "rows is not found."
