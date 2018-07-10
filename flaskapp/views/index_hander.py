#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 1:39
# @Author  : TOM.LEE
# @File    : index_hander.py
# @Software: PyCharm
from flask import Blueprint, flash, render_template


index = Blueprint('index', __name__)


@index.route('/', methods=["GET", "POST"])
def home():
    """
    使用flash来进行消息提示推送
    页面使用{{ get_flashed_messages()[0] }} 获取
    """
    flash("welcome !")
    return render_template("index.html")
