#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-12 下午2:13
# @Author         : Tom.Lee
# @File           : banner.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import getpass
import os
import platform

import flask

banner_text = """
  _________      _____            __          _______     ___  ____
 |_   ___  |    |_   _|          /  \        /  ___  |   |_  ||_  _|
   | |_  \_|      | |           / /\ \      |  (__ \_|     | |_/ /
   |  _|          | |   _      / ____ \      '.___`-.      |  __'.
  _| |_          _| |__/ |   _/ /    \ \_   |`\____) |    _| |  \ \_
 |_____|        |________|  |____|  |____|  |_______.'   |____||____|

Python Version          : {}
Flask Framework Version : {}
Running Environment     : {}
Start The User          : {}

""".format(platform.python_version(), flask.__version__, platform.platform(), getpass.getuser())


def _banner():
    banner_path = os.path.join(
        os.path.dirname(os.path.dirname(
            os.path.dirname(__file__))), 'banner.txt')
    if os.path.exists(banner_path) and os.path.isfile(banner_path):
        with open(banner_path) as f:
            for line in f:
                print(line.rstrip('\n'))
    else:
        print(banner_text)


init = _banner
