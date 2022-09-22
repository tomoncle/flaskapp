#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 15:13
# @Author  : tomoncle
# @Site    : https://github.com/tomoncle/flaskapp
# @File    : session_server01.py
# @Software: PyCharm
"""
flask 默认使用 client cookie 来管理会话, 所以使用 LB 时，可以直接挂nginx
"""
# nginx.conf 配置

# http {
#     ...
#
#     upstream server_group {
#          server 192.168.181.1:5001;
# 	       server 172.16.100.203:5002;
#     }
#     server {
# 	        listen       5000;
# 		    server_name  localhost;
#
# 		    location / {
# 			    index  index.html index.htm;
# 			    proxy_pass http://server_group;
# 		    }
#     }
#     ...
# }
#

from flask import Flask, render_template, request, session, flash, redirect

import config

app = Flask(__name__)

app.config.from_object(config)
app.template_folder = config.TEMPLATE_FOLDER
app.static_folder = config.STATIC_FOLDER
# 使用消息提示需要指定secret_key
app.secret_key = '1!@#$%^&*()'
# 默认情况下session.permanent 是为False的,即浏览器关闭后自动消失
# session.permanent = True


@app.route('/', methods=["GET", "POST"])
def index():
    """
    使用flash来进行消息提示推送
    页面使用{{ get_flashed_messages()[0] }} 获取
    """
    flash("welcome !")
    return render_template("index.html")


@app.route("/logout", methods=["GET","POST"])
def logout():
    session.pop('user01')
    return redirect("/login")


@app.before_request
def interceptor():
    print("init .server02....interceptor {}".format(session.get("user01", None)))
    allow_path = ['/login']
    if request.path in allow_path:
        # pass allow paths
        return

    if session.get("user01", None):
        # if login success , pass
        return

    return redirect("/login")


@app.route('/login', methods=["GET", "POST"])
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
    elif username == 'admin' or 'tom' and password == '123456':
        session.setdefault('user01', username)
        return redirect("/home")
    else:
        flash("username or password is error!")
        return render_template("index.html")


@app.route('/home', methods=["GET"])
def home():
    flash("Congratulations {} login success! server 02".format(session.get("user01")))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)
