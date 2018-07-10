#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 17-11-9 上午10:58
# @Author         : Tom.Lee
# @File           : rest_api.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import random

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! flask'


@app.route('/random')
def random_num():
    """
    flask 只能返回字符串数据
    :return:
    """
    return '%s' % random.random()


@app.route('/data')
def data():
    body = {'message': 'hello world!'}
    headers = dict(request.headers)
    return jsonify({'code': 200, 'headers': headers, 'body': body})


@app.route('/<string:version>/response/<string:api_name>', methods=['POST', 'GET'])
def response(version, api_name):
    """
    http://localhost:5000/v1/response/java9
    :param version:
    :param api_name:
    :return:
    """
    body = {'version': version, 'api_name': api_name}
    headers = dict(request.headers)
    return jsonify({'code': 200, 'headers': headers, 'body': body})


if __name__ == '__main__':
    app.run(debug=True)
