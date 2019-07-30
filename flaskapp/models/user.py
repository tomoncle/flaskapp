#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 22:08
# @Author  : TOM.LEE
# @File    : user.py
# @Software: PyCharm
from .base import DictModel
from flaskapp import db


class User(db.Model, DictModel):
    __tablename__ = 't_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    clazz_id = db.Column(db.Integer, db.ForeignKey('t_class.id'))

    def __init__(self, **kwargs):
        self.username = kwargs.pop('username', None)
        self.email = kwargs.pop('email', None)

    def __repr__(self):
        return '<User %r>' % self.username

        # def json(self, lazy=False, ignore='clazz_id', deep=1):
        #     return super(User,self).json(ignore=ignore)
