#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午2:45
# @Author         : Tom.Lee
# @File           : error_handler.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


from flask import Blueprint, abort

error = Blueprint('error', __name__, url_prefix='/err')


@error.route('/bad_request')
def bad_request():
    abort(400, 'username is required.')


@error.route('/unauthorized')
def unauthorized():
    abort(401, u'没有请求资源的权限')


@error.route('/forbidden')
def forbidden():
    abort(403)


@error.route('/not_found')
def not_found():
    abort(404)


@error.route('/server_error')
def server_error():
    abort(500)


@error.route('/bad_gateway')
def bad_gateway():
    abort(502)


@error.route('/service_unavailable')
def service_unavailable():
    abort(503)


@error.route('/bad_gateway_timeout')
def bad_gateway_timeout():
    abort(504)
