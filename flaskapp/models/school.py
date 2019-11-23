#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/9 22:42
# @Author  : TOM.LEE
# @File    : school.py
# @Software: PyCharm
from .base import DictModel
from flaskapp import db


class School(db.Model, DictModel):
    __tablename__ = 't_school'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(80), nullable=False)
    # 该属性查询"Clazz"时，
    # db.backref('school', lazy='joined')该属性会级联把School类的信息查询出来，
    # 并赋值给backref的第一个参数即"clazz",关联类(Clazz)会自动添加一个动态属性school
    classes = db.relationship('Clazz', backref=db.backref('school', lazy='joined'), lazy='dynamic')

    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)
        self.address = kwargs.pop('address', None)

    def __repr__(self):
        return '<School %r>' % self.name
