#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 9:42
# @File    : 3.py
# @author  : dfkai
# @Software: PyCharm
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/home")
def home():
    return "Hello"


@app.before_request
def be1():
    print("be1")
    # return "出错了"
    return None


@app.before_request
def be2():
    print("be2")
    return None


@app.after_request
def af1(res):
    print("af1")
    return res


@app.after_request
def af2(res):
    print("af2")
    # return res
    return "出错了"


if __name__ == '__main__':
    app.run()