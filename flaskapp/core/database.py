#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 20:52
# @Author  : TOM.LEE
# @File    : database.py
# @Software: PyCharm
from flaskapp import db
from ..common import ConsoleLogger, relative_path, MySQLDataError

__all__ = ['Persistence', 'Modify', 'Modify2', 'Remove', 'Query', 'Query2']

logger = ConsoleLogger(name=relative_path(__file__))


class Database(object):
    """
    database interface
    """


class Transactional(Database):
    def __init__(self, **kwargs):
        """
        事务层
        :param auto_commit: 是否自动提交
        """
        self._auto_commit = kwargs.get('auto_commit', True)
        self.model = kwargs.get('model_class')
        if not self.model:
            raise AssertionError('<class {}>: Required parameter model_class is not present.'
                                 .format(self.__class__.__name__))
        self.session = db.session
        # logger.info('init Transactional')

    def auto_commit(self):
        """
        是否自动提交事务
        :return:
        """
        if self._auto_commit:
            self.session.commit()

    def _check_type(self, obj):
        if not isinstance(obj, self.model):
            raise AssertionError('obj must be <class {}> type.'
                                 .format(self.model.__class__.__name__))

    def __del__(self):
        self.session.remove()
        logger.info("调用删除方法： self.session.remove()")


class Persistence(Transactional):
    def __init__(self, **kwargs):
        super(Persistence, self).__init__(**kwargs)
        # logger.info('init Persistence')

    def _load(self, obj):
        self._check_type(obj)
        self.session.add(obj)

    def save(self, obj):
        # 理论上该方法可以被任意对象使用
        self._load(obj)
        self.auto_commit()
        return obj

    def batch_save(self, arr):
        [self._load(obj) for obj in arr]
        self.auto_commit()
        return arr


class Modify(Transactional):
    def __init__(self, **kwargs):
        super(Modify, self).__init__(**kwargs)
        # logger.info('init Modify')

    def _flush(self, primary_key, obj_dict):
        if not isinstance(obj_dict, dict):
            raise AssertionError('obj_dict must be dict type.')
        obj = self.model.query.get(primary_key)
        if not obj:
            raise MySQLDataError(message='row not found for primary_key {}.'
                                 .format(primary_key))
        for filed in obj_dict:
            setattr(obj, filed, obj_dict[filed])
        return obj

    def update(self, primary_key, obj_dict):
        obj = self._flush(primary_key, obj_dict)
        self.auto_commit()
        return obj

    def batch_update(self, arr):
        data = [self._flush(primary_key, obj_dict) for primary_key, obj_dict in arr]
        self.auto_commit()
        return data


class Remove(Transactional):
    def __init__(self, **kwargs):
        super(Remove, self).__init__(**kwargs)
        # logger.info('init Remove')

    def _del(self, primary_key):
        obj = self.model.query.get(primary_key)
        if not obj:
            raise MySQLDataError(message='row not found for primary_key {}.'
                                 .format(primary_key))
        self.session.delete(obj)
        return primary_key

    def delete(self, primary_key):
        data = self._del(primary_key)
        self.auto_commit()
        return data

    def batch_delete(self, arr):
        data = [self._del(primary_key) for primary_key in arr]
        self.auto_commit()
        return data


class Query(Database):
    def __init__(self, **kwargs):
        # logger.info('init Query')
        self.model = kwargs.get('model_class', None)
        if not self.model:
            raise AssertionError('<class {}>: model_class is not found.'
                                 .format(self.__class__.__name__))

    def _build_query(self, limit=-1, order_by=None, filters=None):
        _query = self.model.query
        if limit > 0:
            _query = _query.limit(limit)
        if order_by and getattr(self.model, order_by, None):
            _query = _query.order_by(getattr(self.model, order_by))

        filters = filters or []
        for _filter in filters:
            _query = _query.filter(_filter)

        return _query

    def _item(self, items):
        if not items:
            return items
        call_json = getattr(self.model, 'json', None)
        if isinstance(items, (list, tuple, set)):
            return [call_json(i) for i in items] if call_json else items
        return call_json(items) if call_json else items

    def get(self, primary_key):
        return self._item(self._build_query().get(primary_key))

    def query_all(self, limit=-1, order_by=None):
        return self._item(self._build_query(limit=limit, order_by=order_by).all())

    def query_filter_all(self, **kwargs):
        return self._item(self._build_query().filter_by(**kwargs).all())

    def query_filter_first(self, **kwargs):
        return self._item(self._build_query().filter_by(**kwargs).first())

    def query_filters(self, filters=None):
        if not filters:
            return self.query_all()
        assert isinstance(filters, (list, tuple, set))
        return self._item(self._build_query(filters=filters).all())

    def count(self, filters=None, **kwargs):
        return self._build_query(filters=filters).filter_by(**kwargs).count()


class Modify2(Database):
    @classmethod
    def _auto_commit(cls):
        db.session.commit()

    @classmethod
    def _flush(cls, model, primary_key, obj_dict):
        if not isinstance(obj_dict, dict):
            raise AssertionError('obj_dict must be dict type.')
        obj = model.query.get(primary_key)
        if not obj:
            raise MySQLDataError(message='row not found for primary_key {}.'
                                 .format(primary_key))
        for filed in obj_dict:
            setattr(obj, filed, obj_dict[filed])
        return obj

    def update(self, model, primary_key, obj_dict):
        obj = self._flush(model, primary_key, obj_dict)
        self._auto_commit()
        return obj

    def batch_update(self, model, arr):
        data = [self._flush(model, primary_key, obj_dict) for primary_key, obj_dict in arr]
        self._auto_commit()
        return data


class Query2(Database):
    def __init__(self):
        """需要传入实体类型来使用该类"""
        # logger.info('init Query2')

    def _build_query(self, model, limit=-1, order_by=None, filters=None):
        _ = self
        _query = model.query
        if limit > 0:
            _query = _query.limit(limit)
        # 假如属性存在,则加入过滤条件
        if order_by and getattr(model, order_by, None):
            _query = _query.order_by(getattr(model, order_by))

        filters = filters or []
        for _filter in filters:
            _query = _query.filter(_filter)

        return _query

    def _item(self, model, items):
        _ = self
        if not items:
            return items
        call_json = getattr(model, 'json', None)
        if not call_json:
            return items
        if isinstance(items, (list, tuple, set)):
            return [call_json(i) for i in items] if call_json else items
        return call_json(items) if call_json else items

    def get(self, model, primary_key):
        return self._item(model, self._build_query(model).get(primary_key))

    def query_all(self, model, limit=-1, order_by=None):
        return self._item(model, self._build_query(model, limit=limit, order_by=order_by).all())

    def query_filter_all(self, model, **kwargs):
        """query_filter_all(username='admin')"""
        return self._item(model, self._build_query(model).filter_by(**kwargs).all())

    def query_filter_first(self, model, **kwargs):
        return self._item(model, self._build_query(model).filter_by(**kwargs).first())

    def query_filters(self, model, filters=None):
        if not filters:
            return self.query_all(model)
        assert isinstance(filters, (list, tuple, set))
        return self._item(model, self._build_query(model, filters=filters).all())
