#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-6-8 上午9:32
# @Author         : Tom.Lee
# @File           : fib.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

import time

from functools32 import lru_cache


@lru_cache()
def fib(n):
    x, y = 0, 1
    for _ in xrange(n):
        x, y = x + y, x
    return x


def fib2(n):
    x, y = 0, 1
    for _ in xrange(n):
        x, y = x + y, x
    return x


start = time.time()

print fib(16)
print 'cache   time: ', time.time() - start
print fib2(16)
print 'uncache time: ', time.time() - start
