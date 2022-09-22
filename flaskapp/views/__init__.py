#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午3:18
# @Author         : Tom.Lee
# @File           : __init__.py.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from .async_handler import cly as _cly
from .error_handler import error as _error
from .index_hander import index as _index
from .rest_clazz_handler import clazz as _clazz
from .rest_login_handler import login as _login
from .rest_school_handler import school as _school
from .rest_user_handler import user as _user
from ..common import ConsoleLogger, relative_path

logger = ConsoleLogger(relative_path(__file__))
logger.info('initial app views model')

BLUEPRINT_MODELS = [
    _error,
    _index,
    _login,
    _user,
    _clazz,
    _school,
    _cly,
]
