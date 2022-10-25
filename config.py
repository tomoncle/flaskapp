#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author         : Tom.Lee
# @File           : settings.py
# @Product        : PyCharm

import os

environ = os.environ
PROJECT_PATH = os.path.dirname(__file__)
TEMPLATE_FOLDER = os.path.join(PROJECT_PATH, "templates")
STATIC_FOLDER = os.path.join(PROJECT_PATH, "static")
DEBUG = True  # open debug /or hot restart

# ****** 上传配置
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'sql'}

# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# ****** MySQL 配置
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(
    user=environ.get('DB_USER', 'DB_USER'),
    password=environ.get('DB_PASS', 'DB_PASS'),
    host=environ.get('DB_HOST', 'DB_HOST'),
    port=environ.get('DB_PORT', 3306),
    database=environ.get('DB_NAME', 'DB_NAME'))
SQLALCHEMY_TRACK_MODIFICATIONS = True  # 禁止警告
SQLALCHEMY_ECHO = False  # 是否打印
# SQLALCHEMY_POOL_SIZE = 15  # 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
# SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是 10。
# SQLALCHEMY_POOL_RECYCLE = 60 * 60 * 2  # 自动回收连接的秒数。
# SQLALCHEMY_MAX_OVERFLOW = 0  # 控制在连接池达到最大值后可以创建的连接数。
SQLALCHEMY_POOL_SIZE = 30  # 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是 10。
SQLALCHEMY_POOL_RECYCLE = 60 * 60 * 2  # 自动回收连接的秒数。
SQLALCHEMY_MAX_OVERFLOW = 20  # 控制在连接池达到最大值后可以创建的连接数。

# ****** Celery 配置 celery.app.utils.py
REDIS_HOST = os.environ.get('REDIS_HOST', 'REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', '')
REDIS_DB = os.environ.get('REDIS_DB', '0')
if REDIS_PASSWORD:
    CELERY_RESULT_BACKEND = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
    CELERY_BROKER_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
else:
    CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
    CELERY_BROKER_URL = f'redis://{REDIS_PORT}/{REDIS_DB}'

# ############################## flask project auto config ######################################
DOWNLOAD_FOLDER = '/tmp'
HOME_PATH = '/'

# ############################## flask start config ######################################
HOST = '0.0.0.0'
PORT = 5000
