#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/23 10:18
# @File    : 装饰器.py
# @author  : dfkai
# @Software: PyCharm
from collections import OrderedDict
from functools import wraps

all_dict = OrderedDict()


def dec(fn):
    @wraps(fn)
    def _wraps(*args, **kwargs):
        if 'xx' in all_dict:
            return all_dict["xx"]
        data = fn(*args, **kwargs)
        all_dict["xx"] = data
        return data

    return _wraps


@dec
def good(hello):
    print(hello)
    return hello


for i in range(5):
    good("hello")
