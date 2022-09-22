#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-25 上午10:07
# @Author         : Tom.Lee
# @File           : async_handler.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from flask import Blueprint

from ..common import json_encoder
from ..plugins import celery

cly = Blueprint('celery', __name__, url_prefix='/task')


@celery.task()
def async_compute(a, b):
    from time import sleep
    sleep(10)
    return a + b


@cly.route('/compute')
@json_encoder
def task():
    result = async_compute.delay(1, 2)
    print(result.wait())
    return 'task id: {}'.format(result)
