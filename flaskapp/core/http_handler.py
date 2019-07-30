#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-11 上午11:06
# @Author         : Tom.Lee
# @File           : http_handler.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from flask import request

from flaskapp import app
from ..common import (view_html, ConsoleLogger, make_response, json_encoder, relative_path)

logger = ConsoleLogger(name=relative_path(__file__))


def is_browser():
    return 'text/html' in '%s' % request.accept_mimetypes


@app.errorhandler(400)
def bad_request(e):
    return view_html(400, e) if is_browser() else make_response(400, e)


@app.errorhandler(401)
def unauthorized(e):
    return view_html(401, e) if is_browser() else make_response(401, e)


@app.errorhandler(403)
def forbidden(e):
    return view_html(403, e) if is_browser() else make_response(403, e)


@app.errorhandler(404)
def not_found(e):
    return view_html(404, e) if is_browser() else make_response(404, e)


@app.errorhandler(405)
def not_allowed(e):
    return view_html(405, e) if is_browser() else make_response(405, e)


@app.errorhandler(500)
def server_error(e):
    logger.error(e)
    return view_html(500, e) if is_browser() else make_response(500, e)


@app.errorhandler(502)
def bad_gateway(e):
    return view_html(502, e) if is_browser() else make_response(502, e)


@app.errorhandler(503)
def service_unavailable(e):
    return view_html(503, e) if is_browser() else make_response(503, e)


@app.errorhandler(504)
def bad_gateway_timeout(e):
    return view_html(504, e) if is_browser() else make_response(504, e)


@app.errorhandler(Exception)
def server_exception(e):
    if not app.config.get('DEBUG', True):  # 如果开启debug打印完整错误信息.
        e = e.message
    return view_html(500, e) if is_browser() else make_response(500, e)


@app.route('/paths')
@json_encoder
def paths():
    data = list(set([url.rule for url in app.url_map.iter_rules()]))
    data.sort()
    return {'paths': data}
