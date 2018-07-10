#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 16:25
# @Author  : TOM.LEE
# @File    : __init__.py.py
# @Software: PyCharm
import database
import http_handler
import http_interceptor
from ..common import ConsoleLogger, relative_path

logger = ConsoleLogger(relative_path(__file__))
logger.info('initial app core model')
