#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-5 下午1:03
# @Author         : Tom.Lee
# @File           : base.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from ..core.database import ( Modify, Persistence,Remove, Query)


class DBService(Persistence, Remove, Modify, Query):
    """
    抽象数据库交互
    """

    def __init__(self, model, auto_commit=True):
        assert model
        super(DBService, self).__init__(auto_commit=auto_commit, model_class=model)
        Query.__init__(self,model_class=model)

    def check_type(self, obj):
        if not isinstance(obj, self.model):
            raise AssertionError('object type must be init model type.')


class AbstractDBService(object):
    def save(self, obj):
        # 理论上该方法可以被任意对象使用
        raise NotImplementedError

    def batch_save(self, arr):
        raise NotImplementedError

    def update(self, primary_key, obj_dict):
        raise NotImplementedError

    def batch_update(self, arr):
        raise NotImplementedError

    def delete(self, obj):
        raise NotImplementedError

    def batch_delete(self, arr):
        raise NotImplementedError

    def get(self, model, primary_key):
        raise NotImplementedError

    def query_all(self, model, limit=-1, order_by=None):
        raise NotImplementedError

    def query_filter_all(self, model, **kwargs):
        """query_filter_all(username='admin')"""
        raise NotImplementedError

    def query_filter_first(self, model, **kwargs):
        raise NotImplementedError

    def query_filters(self, model, filters=None):
        raise NotImplementedError
