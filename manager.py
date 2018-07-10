#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-7-10 上午10:22
# @Author         : Tom.Lee
# @File           : manager.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


import sys

from flaskapp import app
from flaskapp import manager

if __name__ == '__main__':
    # 初始化
    #     $ python manager.py db init
    # 创建/更新表
    #     $ python manager.py db migrate
    # 升级/迁移
    #     $ python manager.py db upgrade
    # 降级
    #     $ python manager.py db downgrade
    # 其他
    #     $ python manager.py db --help
    # runserver
    #     $ python manager.py runserver
    # shell
    #     $ python manager.py shell
    commands = sys.argv
    if len(commands) == 2 and 'runserver' == commands[1]:
        app.start()
    else:
        manager.run()
