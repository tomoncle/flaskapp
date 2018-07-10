#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-13 下午12:52
# @Author         : Tom.Lee
# @File           : bootstrap_celery.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import os

commands = [
    'celery',
    '-A',
    'flaskapp.plugins.celery',
    'worker',
    '--loglevel=debug'
]

try:
    os.system(' '.join(commands))
except KeyboardInterrupt:
    pass
