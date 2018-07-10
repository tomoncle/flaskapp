#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-13 上午9:49
# @Author         : Tom.Lee
# @File           : celery.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from celery import Celery


def make_celery(self, backend=None, broker=None):
    if backend:
        self.config['CELERY_RESULT_BACKEND'] = backend
    if broker:
        self.config['CELERY_BROKER_URL'] = broker
    celery = Celery(
        self.import_name,
        backend=self.config['CELERY_RESULT_BACKEND'],
        broker=self.config['CELERY_BROKER_URL']
    )
    celery.conf.update(self.config)

    class ContextTask(celery.Task):
        def __call__(s, *args, **kwargs):
            with self.app_context():
                return s.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
