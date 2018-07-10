#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-13 上午9:48
# @Author         : Tom.Lee
# @File           : test_celery.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


from celery import Celery
from flask import Flask


def make_celery(app):
    _celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    _celery.conf.update(app.config)

    class ContextTask(_celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    _celery.Task = ContextTask
    return _celery


flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)


@celery.task()
def add_together(a, b):
    return a + b


result = add_together.delay(23, 42)
# result.wait()  # 65
