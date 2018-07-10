#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author         : Tom.Lee
# @File           : bootstrap_app.py
# @Docs           : main


from flaskapp import app

if __name__ == "__main__":
    app.start()
    # app.start(port=5258, debug=False)
