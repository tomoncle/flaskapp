#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午2:51
# @Author         : Tom.Lee
# @File           : rest_clazz_handler.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from flask import Blueprint, request

from ..common.logger import ConsoleLogger
from ..common.response import HttpStatus, make_response
from ..common.tools import relative_path
from ..services import ClazzService


clazz = Blueprint('clazz', __name__, url_prefix='/api/classes')

clazz_service = ClazzService()
logger = ConsoleLogger(name=relative_path(__file__))


@clazz.route('/', methods=["GET", "POST"])
def lists():
    """
    获取users列表
    """
    user_id = request.args.get('id')  # 使用url传参方式 /user?id=xxx
    if user_id:
        return make_response(HttpStatus.SUCCESS, data=clazz_service.get(user_id))
    return make_response(HttpStatus.SUCCESS, data=clazz_service.query_all())


@clazz.route("/<clazz_id>", methods=["GET"])
def get(clazz_id):
    """
    # 使用url传参方式 /users/xxx

    根据user id 获取user对象
    :param clazz_id: 参数使用<user_id>获取
    """
    # if not user_id:
    #     abort(404)  # 假如 id为空,抛出404异常
    _user = clazz_service.get(clazz_id)
    return make_response(HttpStatus.SUCCESS, data=_user)
