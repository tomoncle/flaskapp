#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-11 上午10:44
# @Author         : Tom.Lee
# @File           : http_interceptor.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from flask import request

from flaskapp import app
from ..common import ConsoleLogger

logger = ConsoleLogger(name='http_interceptor')


@app.before_request
def before_interceptor():
    args = request.args or request.data or request.form
    logger.debug('request params: [%s]'.format(args))


@app.after_request
def process_response(response):
    # logger.debug('response status: [%s]' % response.status)
    return response
