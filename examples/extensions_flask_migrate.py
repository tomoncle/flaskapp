#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-7-10 上午9:27
# @Author         : Tom.Lee
# @File           : extensions_flask_migrate.py
# @Product        : PyCharm
# @Source         : 


from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)


if __name__ == '__main__':
    """
    初始化
    $ python extensions_flask_migrate.py db init

    创建/更新表
    $ python extensions_flask_migrate.py db migrate

    升级/迁移
    $ python extensions_flask_migrate.py db upgrade

    降级
    $ python extensions_flask_migrate.py db downgrade

    其他
    $ python extensions_flask_migrate.py db --help
    """
    manager.run()
