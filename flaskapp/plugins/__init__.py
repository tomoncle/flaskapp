#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-13 下午2:52
# @Author         : Tom.Lee
# @File           : __init__.py.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from .flask_celery import Celery, make_celery

celery = Celery()
__all__ = ['celery', 'make_celery']
