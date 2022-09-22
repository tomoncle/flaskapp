#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author         : Tom.Lee
# @File           : tools.py
# @Product        : PyCharm
# @Docs           : main
# @Source         :
from flask import Flask, Blueprint
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

import config
from . import common
from . import extends
from . import plugins

logger = common.ConsoleLogger('flask')

app = Flask(__name__)
app.static_folder = config.STATIC_FOLDER
app.template_folder = config.TEMPLATE_FOLDER
app.secret_key = '1!@#$%^&*()'
app.config.from_object(config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def __register_blueprint_models():
    # 注册模块信息
    try:
        from .views import BLUEPRINT_MODELS
        if not isinstance(BLUEPRINT_MODELS, (tuple, list, set)):
            raise AssertionError('BLUEPRINT_MODELS must be (tuple, list, set) type.')
    except (ImportError, AssertionError, Exception) as e:
        logger.warning('register blueprint fail, {}'.format(e))
        return

    for model in BLUEPRINT_MODELS:
        if not isinstance(model, Blueprint):
            logger.error('Register Blueprint {} model fail, '
                         'The model type must be flask.Blueprint.'.format(model))
            continue
        try:
            app.register_blueprint(model)
            logger.info('register blueprint {} success.'.format(model.name))
        except Exception as e:
            logger.error('register blueprint {} error, {}.'.format(model.name, e))


def __init_tables():
    db.create_all()


def __flask_extends():
    setattr(Flask, 'make_celery', plugins.make_celery)
    plugins.celery = app.make_celery()


__flask_extends()
__register_blueprint_models()
__init_tables()
logger.debug("urls: ")
for i in list(set([url.rule for url in app.url_map.iter_rules()])):
    logger.debug(i)
