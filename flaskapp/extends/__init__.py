#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-12 上午11:03
# @Author         : Tom.Lee
# @File           : __init__.py.py
# @Product        : PyCharm
# @Docs           :
# @Source         : 

from . import functions

setattr(functions.Flask, 'start', functions.start)
setattr(functions.Config, 'from_properties', functions.from_properties)

