#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-25 上午10:14
# @Author         : Tom.Lee
# @File           : test_celery_task.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 


import requests

response = requests.get('http://localhost:8080/task/compute')

print response.status_code
print response.content
