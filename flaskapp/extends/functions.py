#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-12 下午1:25
# @Author         : Tom.Lee
# @File           : functions.py
# @Product        : PyCharm
# @Docs           : flask 配置拓展函数.
# @Source         : 
import os
import time

from flask import Flask, Config

from . import banner
from ..common import LoggerFactory

_x, _y, _t, _delay = Flask, Config, time.time(), 0.05
logger = LoggerFactory.logger('Listener')


def start(self, host=None, port=None, debug=None, **options):
    banner.init()
    time.sleep(_delay)

    host = host or self.config.get('HOST', None)
    port = port or self.config.get('PORT', None)
    debug = self.config.get('DEBUG', None) if debug is None else debug
    logger.info('[{}] bootstrap init on http://{}:{}/. Start used time : {} s'.format(
        self.name, host, port, time.time() - _t - _delay))
    try:
        self.run(host=host, port=port, debug=debug, **options)
    except KeyboardInterrupt:
        pass


def from_properties(self, file_path):
    environ = os.environ
    with open(file_path) as f:
        for line in f:
            if line.startswith('#'):
                continue
            line = line.rstrip('\n').replace(' ', '')
            if not line:
                continue
            key, value = tuple(line.rstrip('\n').split('='))
            if value.startswith('${') and value.endswith('}'):
                args = tuple(value.lstrip('${').rstrip('}').split(':'))
                value = environ.get(*args)

            self[key] = value
