#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午2:51
# @Author         : Tom.Lee
# @File           : rest_clazz_handler.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from flask import Blueprint, request

from ..common import (ConsoleLogger, make_response, HttpError,
                      relative_path, multi_dict_parser2dict)
from ..models import School
from ..services import DBService

school = Blueprint('school', __name__, url_prefix='/api/schools')

school_service = DBService(model=School)
logger = ConsoleLogger(name=relative_path(__file__))


@school.route('/', methods=["GET", "POST", "PUT"])  # 匹配/api/schools
def lists():
    """
    匹配多种路径：
        /api/schools
        /api/schools/

    获取users列表
    """
    method = request.method
    if method == 'GET':
        user_id = request.args.get('id')  # 使用url传参方式 /user?id=xxx
        if user_id:
            return make_response(data=school_service.get(user_id))
        return make_response(data=school_service.query_all())

    elif method == 'POST':
        obj = school_service.save(School(**multi_dict_parser2dict(request.form)))
        return make_response(data=obj.json())

    elif method == 'PUT':
        obj_dict = multi_dict_parser2dict(request.form)
        primary_key = obj_dict.pop('id', None)
        if not primary_key:
            HttpError.bad_request('id')
        obj = school_service.update(primary_key=primary_key, obj_dict=obj_dict)
        return make_response(data=obj.json())
    else:
        HttpError.not_allowed()


@school.route("/<school_id>", methods=["GET", "DELETE"])
def get(school_id):
    """
    # 使用url传参方式 /users/xxx

    根据user id 获取user对象
    :param school_id: 参数使用<school_id>获取
    """
    # if not user_id:
    #     abort(404)  # 假如 id为空,抛出404异常
    if request.method == 'DELETE':
        return make_response(data=school_service.delete(school_id))
    _user = school_service.get(school_id)
    return make_response(data=_user)


@school.route("/count", methods=["GET"])
def count():
    """
    # 使用url传参方式 /users/xxx

    根据user id 获取user对象
    :param school_id: 参数使用<school_id>获取
    """
    # if not user_id:
    #     abort(404)  # 假如 id为空,抛出404异常
    return make_response(data=school_service.count())
