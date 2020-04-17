#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 10:15
# @File    : 1.py
# @author  : dfkai
# @Software: PyCharm
### 1
data = sum(range(1, 101))
print(data)

### 4

a = {
    'kk': 1
}

b = {
    'ff': 2
}
del a['kk']

a.update(b)

print(a)
### 6
c = [1, 2, 2, 3, 4, 5, 5, 6, 6]
print(list(set(c)))

### 13
a = [1, 2, 3, 4, 5]
b = list(filter(lambda x: x > 10, map(lambda x: x * x, a)))
print(b)

### 14
from random import randint, random

import numpy as np

# 随机整数
c = randint(0, 1)
# 生成五个随机小数 正负皆有
c2 = np.random.randn(5)
c3 = random()  # 0-1 随机小数
print(c, c2, c3)

### 16
import re

v = '<div class="nam">中国</div>'
# c = re.findall(r'<div class=".*">(.*?)</div>', v)
# c = re.findall(r'<div class=".*?">(.*?)</div>', v)
c = re.match(r'<div class=".*?">(.*?)</div>', v).group(1)
print(c)

### 17

assert 1 == True

assert isinstance(1, int)

### 18
"select distinct name from student"

### 19
"ls df ps yum apt cat vi free mv cp grep echo mkdir rm touch cd"

### 20、python2和python3区别？列举5个
"""
1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')
Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比 如 print 'hi'
2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存
3、python2中使用ascii编码，python中使用utf-8编码
4、python2中unicode表示字符串序列，str表示字节序列
python3中str表示字符串序列，byte表示字节序列
5、python2中为正常显示中文，引入coding声明，python3中不需要
6、python2中是raw_input()函数，python3中是input()函数
"""

### 21
"可变数据类型：列表list和字典dict；"
"不可变数据类型：数值型、字符串型string和元组tuple"

### 22
s = "ajldjlajfdljfddd"
c = list(set(s))
c.sort()
print("".join(c))
### 23
acc = lambda a, b: a * b
print(acc(1, 2))

### 24
dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
lis = sorted(dic.items(), key=lambda i: i[0], reverse=False)
print(lis)
print(dict(lis))

### 25
from collections import Counter

c = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
a = Counter(c)
print(a.items())
### 26
a = "not 404 found 张三 99 深圳"
lis = a.split(" ")
c = re.findall('\d+|[a-zA-Z]+', a)
print(c)
d = " ".join(list(filter(lambda x: x not in c, lis)))
print(d)
### 27
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = list(filter(lambda x: x % 2 == 1, a))
print(c)

### 29、正则re.complie作用
're.compile是将正则表达式编译成一个对象，加快速度，并重复使用'

### 30
a = (1,)
print(type(a))
b = (1)
print(type(b))
c = ("1")
print(type(c))
"""
<class 'tuple'>
<class 'int'>
<class 'str'>
"""

# ### 32
# import os
#
# path = "xxx"
# os.remove(path)
# # rm
# os.system(f"rm {path}")

### 33
from datetime import datetime

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('星期', str(datetime.now().isoweekday()))
print('星期', str(datetime.now().isocalendar()))

### 35 请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行
"""pyecharts、matplotlib"""

### 39
a = [[1, 2], [3, 4], [5, 6]]
c = [z for j in a for z in j]
print(c)

import numpy as np

b = np.array(a).flatten().tolist()
print(b)

x = "abc"
y = "def"
z = ["d", "e", "f"]
print(x.join(y))
print(x.join(z))

# 41

"raise finally"
try:
    1 / 0
except Exception as e:
    print('raise')
else:
    print("else")
finally:
    print('finally')

"else finally"
try:
    1 / 1
except Exception as e:
    print('raise')
else:
    print("else")
finally:
    print('finally')

a, b = 3, 4
a, b = b, a
print(a, b)

### 43
a = [1, 2]
c = [3, 4]
res = [i for i in zip(a, c)]
print(res)

a = (1, 2)
c = (3, 4)
res = [i for i in zip(a, c)]
print(res)

a = 'ab'
b = 'xyz'
res = [i for i in zip(a, c)]
print(res)
"""
[(1, 3), (2, 4)]
[(1, 3), (2, 4)]
[('a', 3), ('b', 4)]
"""
### 44
import re

a = "张明 98分"
c = re.sub('\d+', '100', a)
print(c)

### 46
a = 'hello'
b = '你好'
print(bytes(a, encoding='utf8'))
print(bytes(b, encoding='utf8'))

### 48、提高python运行效率的方法
"""
1、使用生成器，因为可以节约大量内存
2、循环代码优化，避免过多重复代码的执行
3、核心模块用Cython PyPy等，提高效率
4、多进程、多线程、协程
5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率
"""
### 51
url = 'https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

import re

pat = re.compile('.*?(\d+-\d+-\d+).*?')
c = pat.findall(url)
print(c)


### 53 单列模式
class Singleton(object):
    # __instance = None
    #
    # def __new__(cls, age, name):
    #     if not cls.__instance:
    #         cls.__instance = object.__new__(cls)
    #     return cls.__instance
    def __new__(cls, age, name):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance


a = Singleton(18, 'dd')
b = Singleton(6, 'd33')

print(id(a))
print(id(b))

a.age = 19
print(b.age)  # 19

### 54
a = "%.03f" % 1.3335
print(a, type(a))
b = round(float(a), 1)
print(b, type(b))
b = round(float(a), 2)
print(b, type(b))


### 55
def fn(k, v, dic={}):
    dic[k] = v
    print(dic)


# 直接将键值对传给字典；
fn("one", 1)
# 因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对
fn("two", 2)
# 因为传了一个新字典，所以不再是原先默认参数的字典
fn("three", 3, {})
"""
{'one': 1}
{'one': 1, 'two': 2}
{'three': 3}
"""

### 68
"python 1.py 22 33"
"print(sys.argv) # 1.py 22 33"

### 69 [i for i in range(3)]改成生成器
"""
生成器是特殊的迭代器，
1、列表表达式的【】改为（）即可变成生成器
2、函数在返回值得时候出现yield就变成生成器，而不是函数了；
"""
### 72
foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
a = sorted(foo, key=lambda x: x)
c = sorted(foo)
print(a)
print(c)

### 73
foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
a = sorted(foo, key=lambda x: x < 0)
c = sorted(foo, key=lambda x: abs(x))
b = sorted(foo, key=lambda x: (x < 0, abs(x)))
print(a)
print(b)
print(c)

### 80
s = ['ab', 'abc', 'a', 'df', 'dfk']
b = sorted(s, key=lambda x: len(x))
print(b)

### 81
# import pymysql
# db = pymysql.connect(host="localhost",user='root',password='123456',db='demo')
# cs = db.cursor()
# input_name = 'zs'
# sql = 'select * from demo where name="%s"' % input_name
# print(sql)
# input_name = 'zs";drop table demo;'
# input_name = pymysql.escape_string(input_name)
# sql = 'select * from demo where name="%s"' % input_name
# print(sql)
# c = cs.execute(sql)
# print(c)

# input_name = 'zs;drop database  demo'
# ar = [input_name]
# c = cs.execute('select * from demo where name=%s',ar)
# print(c)

### 82
import re

s = "info:xiaoZhang 33 shandong"
b = re.split(r':|', s)
print(b)

### 83
a = ['ssasdf@163.com', 'xiaowang@163.xxx', 'xiaowang@163.comsss']
# c = re.compile(r'.*?@163.com$')
c = re.compile(r'[\w]{4,20}@163.com$')
for i in a:
    d = c.match(i)
    if d:
        print(d.group())


### 84
def get_sum(num):
    if num >= 1:
        res = num + get_sum(num - 1)
    else:
        res = 0
    return res


def get_sum_2(num):
    if num <= 0:
        return 0
    return num + get_sum_2(num - 1)


res = get_sum(10)
print(res)

s = get_sum_2(10)
print(s)

### 86
"""
86、MyISAM 与 InnoDB 区别：
1、InnoDB 支持事务，MyISAM 不支持，这一点是非常之重要。事务是一种高级的处理方式，如在一些列增删改中只要哪个出错还可以回滚还原，而 MyISAM就不可以了；
2、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到安全性较高的应用；
3、InnoDB 支持外键，MyISAM 不支持；
4、对于自增长的字段，InnoDB 中必须包含只有该字段的索引，但是在 MyISAM表中可以和其他字段一起建立联合索引；
5、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重建表；
"""


class Animal(object):
    def __init__(self, name):
        print('__init__ 方法被调用')
        self.__name = name

    def __del__(self):
        print('__del__方法被调用')
        print('%s 对象马上被干掉了。' % self.__name)


cat = Animal('波斯猫')
cat2 = cat
cat3 = cat
print(id(cat), id(cat2), id(cat3))
print('cat ')
del cat
print('cat2 ')
del cat2
print('cat3')
del cat3
"""
271246542664 271246542664 271246542664
cat 
cat2 
cat3
__del__方法被调用
波斯猫 对象马上被干掉了。
"""
# 只有在cat 真的被删除才会调用 __del__
print(int('1'))
# int('1.4')  # 只有 字符串 是 十进制才可以被  转换 报错
print(int(1.4))
