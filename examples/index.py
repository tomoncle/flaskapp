#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午3:05
# @Author         : Tom.Lee
# @File           : index.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


"""
第一个flask程序
"""

from flask import Flask, render_template, request, abort, flash, redirect

import config

app = Flask(__name__)

app.config.from_object(config)
app.template_folder = config.TEMPLATE_FOLDER
app.static_folder = config.STATIC_FOLDER
# 使用消息提示需要指定secret_key
app.secret_key = '1!@#$%^&*()'


@app.route('/', methods=["GET", "POST"])
def index():
    """
    使用flash来进行消息提示推送
    页面使用{{ get_flashed_messages()[0] }} 获取
    """
    flash("welcome !")
    return render_template("index.html")


@app.route('/users')
def users():
    """
    获取users列表
    """
    data = ['jack', 'tom', 'jenny']
    return render_template("index.html", users=data)


@app.route("/users/info", methods=["GET"])
def user_info():
    """
    根据 request获取参数
    """
    req_id = request.args.get('id')
    if not req_id:
        abort(404)  # 假如 id为空,抛出404异常
    return render_template("index.html", user="user id:{0}".format(req_id))


@app.route("/user/<user_id>")
def get_user(user_id):
    """
    根据user id 获取user对象
    :param user_id: 参数使用<user_id>获取
    """
    if not user_id:
        abort(404)  # 假如 id为空,抛出404异常
    return render_template("index.html", user="user id:{0}".format(user_id))


@app.errorhandler(404)
def not_fund(e):
    """
    404 页面
    :param e:  必须要传递一个参数, 不管是否使用该参数
    """
    return render_template("404.html", err=e)


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("index.html")

    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash(u"username 不能为空！")
        return render_template("index.html")
    elif not password:
        flash(u"password 不能为空！")
        return render_template("index.html")
    elif username == 'admin' and password == 'admin':
        return redirect("/home")
    else:
        flash("username or password is error!")
        return render_template("index.html")


@app.route('/home', methods=["GET"])
def home():
    flash("login success!")
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
