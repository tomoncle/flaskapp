#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 22:02
# @Author  : TOM.LEE
# @File    : logger.py
# @Software: PyCharm
import logging

FORMAT_STR = '%(asctime)s %(levelname)s {model} :: %(message)s'


class ConsoleLogger(object):
    """
    自定义logger
    examples:
        logger = ConsoleLogger('mode_name')
        logger.info("ok!")
    """

    def __new__(cls, name='%(module)s'):
        __format = '%(asctime)s %(levelname)s {model} :: %(message)s'.format(model=name)
        __logger = logging.getLogger(name)
        __logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(__format)
        handler.setFormatter(formatter)
        __logger.addHandler(handler)
        return __logger


class LoggerFactory(object):
    @staticmethod
    def logger(name='%(module)s'):
        __format = '%(asctime)s %(levelname)s {model} :: %(message)s'.format(model=name)
        __logger = logging.getLogger(name)
        __logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(__format)
        handler.setFormatter(formatter)
        __logger.addHandler(handler)
        return __logger
