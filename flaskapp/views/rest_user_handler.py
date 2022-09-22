#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午2:51
# @Author         : Tom.Lee
# @File           : rest_user_handler.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from flask import Blueprint, request, abort

from ..common.logger import ConsoleLogger
from ..common.response import HttpStatus, make_response
from ..common.tools import relative_path
from ..models import User
from ..services import UserService

user = Blueprint('user', __name__, url_prefix='/api/users')

user_service = UserService()
logger = ConsoleLogger(name=relative_path(__file__))


@user.route('/', methods=["GET", "POST"])
def users():
    """
    获取users列表
    """
    user_id = request.args.get('id')  # 使用url传参方式 /user?id=xxx
    if request.method == 'GET':
        if user_id:
            return make_response(HttpStatus.SUCCESS, data=user_service.get(user_id))
        return make_response(HttpStatus.SUCCESS, data=user_service.query_all())

    import random
    user_name = request.form.get('name') + str(random.random())
    user_email = request.form.get('email') + str(random.random())
    if not all((user_name, user_email)):
        abort(HttpStatus.BAD_REQUEST)
    data = user_service.save(User(username=user_name, email=user_email))
    return make_response(HttpStatus.SUCCESS, data=data.json())


@user.route("/<user_id>", methods=["GET"])
def get(user_id):
    """
    # 使用url传参方式 /users/xxx

    根据user id 获取user对象
    :param user_id: 参数使用<user_id>获取
    """
    # if not user_id:
    #     abort(404)  # 假如 id为空,抛出404异常
    _user = user_service.get(user_id)
    return make_response(HttpStatus.SUCCESS, data=_user)
