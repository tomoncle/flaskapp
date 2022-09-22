#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author         : Tom.Lee
# @File           : tools.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import os
from collections import defaultdict
from functools import reduce

from werkzeug.datastructures import ImmutableMultiDict

from config import (PROJECT_PATH, ALLOWED_EXTENSIONS)

environ = os.environ


def allowed_file(filename):
    """
    >> print allowed_file(abc.jpg)

    :param filename:
    :return:
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def open_file_to_iterable(file_path):
    with open(file_path) as f:
        for line in f:
            yield line


def get_file_bytes(file_path):
    def prod(x, y):
        return x + y

    return reduce(prod, [len(b) for b in open_file_to_iterable(file_path)])


def create_or_pass_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)


def relative_path(f):
    return os.path.realpath(f).replace(
        '\\', '.').replace(
        '/', '.').replace(
        PROJECT_PATH.replace(
            '\\', '.').replace(
            '/', '.'), '').lstrip(
        '.').rstrip(
        '.py').rstrip(
        '.pyc').rstrip(
        '.__init__')


def encapsulation_class(target_class, target_object, func_name_list):
    [setattr(target_class, func_name, getattr(target_object, func_name))
     for func_name in func_name_list
     if getattr(target_object, func_name, None)]


def encapsulation_func(target_class, func):
    assert callable(func)
    setattr(target_class, func.__name__, func)


def parser_properties(file_path):
    properties_data = defaultdict(str)
    with open(file_path) as f:
        for line in f:
            if line.startswith('#'):
                continue
            line = line.rstrip('\n').replace(' ', '')
            if not line:
                continue
            key, value = tuple(line.rstrip('\n').split('='))
            if value.startswith('${') and value.endswith('}'):
                args = tuple(value.lstrip('${').rstrip('}').split(':'))
                value = environ.get(*args)

            properties_data[key] = value
    return properties_data


def multi_dict_parser2dict(multi_dict):
    if not isinstance(multi_dict, ImmutableMultiDict):
        raise AssertionError('object type must be ImmutableMultiDict')
    return {k: multi_dict[k] for k in multi_dict}
