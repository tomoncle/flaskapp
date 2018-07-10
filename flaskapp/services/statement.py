#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 21:17
# @Author  : TOM.LEE
# @File    : statement.py
# @Software: PyCharm

from ..models import User, Clazz
from ..services import DBService


class UserService(DBService):
    def __init__(self):
        super(UserService, self).__init__(model=User)


class ClazzService(DBService):
    def __init__(self):
        super(ClazzService, self).__init__(model=Clazz)
