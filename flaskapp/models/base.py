#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-6 下午5:24
# @Author         : Tom.Lee
# @File           : base.py
# @Product        : PyCharm
# @Docs           : 
# @Source         :

from flask_sqlalchemy import BaseQuery

from ..common.logger import ConsoleLogger
from ..common.tools import relative_path

logger = ConsoleLogger(name=relative_path(__file__))


class DictModel(object):
    """
    添加转json方法
    """

    def json(self, lazy=False, ignore=None, deep=1):
        """
        转化json
        :param lazy: 是否懒加载
        :param ignore: 过滤属性
        :param deep： 当前深度
        :return:
        """
        ignore_filed = ['query', 'metadata'] + ignore if isinstance(ignore, list) else ['query', 'metadata', ignore]

        def _filter_filed(obj):
            return filter(lambda y: all(
                (
                    y not in ignore_filed,
                    not y.endswith('_'),
                    not y.startswith('_'),
                    not callable(getattr(obj, y))
                )), dir(obj))

        def _get_ignore_filed(base_obj, obj, _filed_list):
            _ignore_filed = []
            for _filed in _filed_list:
                _filed_obj = getattr(obj, _filed)
                if isinstance(_filed_obj, BaseQuery):
                    _primary_entity = '%s' % _filed_obj.attr.target_mapper
                    if '|' in _primary_entity and _primary_entity.split('|')[1] == base_obj.__class__.__name__:
                        _ignore_filed.append(_filed)
                    if '->' in _primary_entity and _primary_entity.split('->')[1] == base_obj.__class__.__name__:
                        _ignore_filed.append(_filed)
                if isinstance(_filed_obj, type(base_obj)):
                    _ignore_filed.append(_filed)
            return _ignore_filed

        __relationship__, res, filed_list = None, {}, _filter_filed(self)
        for filed in filed_list:
            filed_type = getattr(self, filed)
            if filed == __relationship__:
                continue
            if isinstance(filed_type, DictModel):
                _ignore = _get_ignore_filed(self, filed_type, _filter_filed(filed_type))
                relationship_model = filed_type.json(ignore=_ignore, deep=deep + 1)
                if not lazy:
                    res[filed] = relationship_model
            elif isinstance(filed_type, (int, list)):
                res[filed] = filed_type
            elif isinstance(filed_type, BaseQuery):
                res[filed] = []
                if not lazy:
                    for f in filed_type.all():
                        _ignore = _get_ignore_filed(self, f, _filter_filed(f))
                        res[filed].append(f.json(lazy=lazy, ignore=_ignore, deep=deep + 1))
            else:
                try:
                    # TODO
                    if isinstance(filed_type, str):
                        filed_type = filed_type  # .encode('UTF-8')
                    if isinstance(filed_type, bytes):
                        filed_type = filed_type.decode('UTF-8')
                    res[filed] = '{}'.format(filed_type)
                except (UnicodeEncodeError, Exception) as e:
                    logger.error('{class_name}.{filed}: {e}'.format(
                        class_name=self.__class__.__name__, filed=filed, e=e))
                    res[filed] = None
        return res
