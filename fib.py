#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 9:51
# @File    : fib.py
# @author  : dfkai
# @Software: PyCharm

def fib_recur(n):
    assert n >= 0, "n > 0"
    if n <= 1:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)


print(fib_recur(3))


def fib_two(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib_two(3))

print("fuckkk")
print("helo")
