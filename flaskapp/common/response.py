#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-5 下午1:24
# @Author         : Tom.Lee
# @File           : response.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
import json
import time
from functools import wraps

from flask import request, jsonify, abort
from flask.globals import current_app


class HttpStatus(object):
    SUCCESS = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    NOT_ALLOWED = 405
    SERVER_ERROR = 500


class HttpError(object):
    @classmethod
    def bad_request(cls, arg=None):
        if not arg:
            abort(HttpStatus.BAD_REQUEST)
        abort(HttpStatus.BAD_REQUEST, "Required parameter '{}' is not present".format(arg))

    @classmethod
    def not_found(cls, arg=None):
        if not arg:
            abort(HttpStatus.NOT_FOUND)
        abort(HttpStatus.NOT_FOUND, "{}".format(arg))

    @classmethod
    def not_allowed(cls, arg=None):
        if not arg:
            abort(HttpStatus.NOT_ALLOWED)
        abort(HttpStatus.NOT_ALLOWED, "{}".format(arg))


def make_response(status=HttpStatus.SUCCESS, e=None, data=None):
    """
    构建返回值信息
    :param status: 状态码
    :param e:　　　 信息
    :param data:   数据
    :return:   json str data
    """
    assert isinstance(status, int)
    if status in range(200, 300) and not e:
        e = 'success'
    if hasattr(e, 'message') and e.message:
        e = e.message
    elif hasattr(e, 'description') and e.description:
        e = e.description
    else:
        e = '{}'.format(e)

    return jsonify({
        'status': status,
        'timestamp': int(round(time.time() * 1000)),
        'data': data,
        'path': request.path,
        'method': request.method,
        'message': '{msg}'.format(msg=e or 'unknown')
    })


def json_encoder(func):
    """
    python obj to json
    :param func:
    :return: json data
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return current_app.response_class(json.dumps(data, indent=2), mimetype='application/json')

    return wrapper
