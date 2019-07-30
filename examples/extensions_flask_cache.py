#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-7-3 下午3:00
# @Author         : Tom.Lee
# @Product        : PyCharm
# @Source         :

"""
$ pip install Flask-Cache
"""

from flask import Flask
from flask.ext.cache import Cache

app = Flask(__name__)
# Check Configuring Flask-Cache section for more details
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


def _call():
    """
    假如缓存生效,则不调用该函数
    反之，打印信息
    :return:
    """
    print('call database...')


@app.route('/')
@cache.cached(timeout=50, key_prefix='data')
def data():
    _call()
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
