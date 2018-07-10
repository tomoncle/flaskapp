#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-11 下午1:47
# @Author         : Tom.Lee
# @File           : test_db.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

from flaskapp import db

# drop table
db.drop_all()

# create table
db.create_all()
