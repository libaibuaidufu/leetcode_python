#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 22:01
# @File    : Insertion_sort.py
# @author  : dfkai
# @Software: PyCharm
# 插入排序 就是 把 左边的列表 以此与右边的数进行对比
# 插入排序 就是 加入 列表中的第一个数 是你手中的牌
# 然后 第二个是你数 是你摸到的牌 如果 你摸到牌大于 你手中最后一张牌 就放在手牌右边 小于 就放在牌左边

source = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]

for index in range(1, len(source)):
    current_val = source[index]  # 先记下来每次大循环走到的第几个元素的值
    position = index

    while position > 0 and source[position - 1] > current_val:  # 当前元素的左边的紧靠的元素比它大,要把左边的元素一个一个的往右移一位,给当前这个值插入到左边挪一个位置出来
        source[position] = source[position - 1]  # 把左边的一个元素往右移一位
        position -= 1  # 只一次左移只能把当前元素一个位置 ,还得继续左移只到此元素放到排序好的列表的适当位置 为止

    source[position] = current_val  # 已经找到了左边排序好的列表里不小于current_val的元素的位置,把current_val放在这里
    print(source)

def insert_sort(li):
   for i in range(1, len(li)): # i是摸到的牌的下标
       tmp = li[i]     # tmp是摸到牌的值
       # 方法一
       j = i - 1 # j是手里最后一张牌的下标    li[j]是手里最后一张牌的值
       while j >= 0 and li[j] > tmp:   # 两个终止条件：j小于0表示tmp是最小的 顺序不要乱
           li[j+1] = li[j]
           j -= 1
       # 方法二
       # for j in range(i-1, -1, -1):
       #     if li[j] > tmp:
       #         li[j+1] = li[j]
       #     else:
       #         break
       li[j+1] = tmp   #将摸到的牌 插入到 往前挪过之后的 j 的后一位