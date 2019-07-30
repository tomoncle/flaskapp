#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-7 上午9:34
# @Author         : Tom.Lee
# @File           : clazz.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 
from .base import DictModel
from flaskapp import db


class Clazz(db.Model, DictModel):
    __tablename__ = 't_class'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # 该属性查询"User"时，
    # db.backref('clazz', lazy='joined')该属性会级联把Clazz类的信息查询出来，
    # 并赋值给backref的第一个参数即"clazz",关联类(User)会自动添加一个动态属性clazz
    users = db.relationship('User', backref=db.backref('clazz', lazy='joined'), lazy='dynamic')
    school_id = db.Column(db.Integer, db.ForeignKey('t_school.id'))

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)

    def __repr__(self):
        return '<Clazz %r>' % self.name
