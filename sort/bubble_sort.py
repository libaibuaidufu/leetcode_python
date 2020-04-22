#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 21:30
# @File    : bubble_sort.py
# @author  : dfkai
# @Software: PyCharm
# 每次比较两个数 把最大的 把最大的每次向后移 最后循环一边后 最大的 就在最后了
# 然后 接着再次循环 第二大的 又像后面 排
# 冒泡排序 主要就是排最大的值 往后靠
data_set = [9, 1, 22, 31, 45, 3, 6, 2, 11]

loop_count = 0
for j in range(len(data_set)):
    # -1 是因为每次比对的都 是i 与i +1,不减1的话,最后一次对比会超出list 获取范围,
    # -j是因为,每一次大loop就代表排序好了一个最大值,放在了列表最后面,下次loop就不用再运算已经排序好了的值 了
    for i in range(len(data_set) - j - 1):
        print(data_set[i], data_set[i + 1])
        if data_set[i] > data_set[i + 1]:  # switch
            data_set[i], data_set[i + 1] = data_set[i + 1], data_set[i]
            # tmp = data_set[i]
            # data_set[i] = data_set[i + 1]
            # data_set[i + 1] = tmp
        loop_count += 1
    print(data_set)
print(data_set)
print("loop times", loop_count)
