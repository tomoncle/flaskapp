# -*- encoding=utf-8 -*-
"""
flask 表单开发,使用wtf插件
pip install flask-wtf
"""

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from wtforms import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms import validators

import config

app = Flask(__name__, static_folder=config.STATIC_FOLDER, template_folder=config.TEMPLATE_FOLDER)


class LoginForm(Form):
    # 登录form 验证字段
    username = StringField('username', [validators.length(3, 50)])
    password = PasswordField('password', [validators.length(3, 50)])


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    登录页面
    :return:
    """
    login_form = LoginForm(request.form)  # 登录form
    if request.method == 'POST':
        if all((login_form.validate(),
                login_form.username.data == 'admin',
                login_form.password.data == 'admin')):
            return redirect('https://www.baidu.com')
        else:
            message = 'login failed'
            return render_template('examples/extensions_flask_form.html',
                                   message=message, form=login_form)
    return render_template('examples/extensions_flask_form.html', form=login_form)


@app.route("/", methods=['GET'])
def index():
    """
    首页
    :return:
    """
    # 重定向到登录页面
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=config.DEBUG)
