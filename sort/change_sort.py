#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 21:50
# @File    : change_sort.py
# @author  : dfkai
# @Software: PyCharm
# 选择排序 每循环一次选出最小的 放在第一位
data_set = [9, 1, 22, 31, 45, 3, 6, 2, 11]

smallest_num_index = 0  # 初始列表最小值,默认为第一个

loop_count = 0
for j in range(len(data_set)):
    for i in range(j, len(data_set)):
        if data_set[i] < data_set[smallest_num_index]:  # 当前值 比之前选出来的最小值 还要小,那就把它换成最小值
            smallest_num_index = i
        loop_count += 1
    else:
        print("smallest num is ", data_set[smallest_num_index])
        tmp = data_set[smallest_num_index]
        data_set[smallest_num_index] = data_set[j]
        data_set[j] = tmp

    print(data_set)
    print("loop times", loop_count)

# for else 当执行完 for后 中途没有continue 就执行else

for j in range(len(data_set)):
    for i in range(j, len(data_set)):  # 循环一次找出最小值所在的索引
        if data_set[i] < data_set[smallest_num_index]:
            smallest_num_index = i
        loop_count += 1
    else:
        data_set[j], data_set[smallest_num_index] = data_set[smallest_num_index], data_set[j]
    print(data_set)
    print("loop times", loop_count)
