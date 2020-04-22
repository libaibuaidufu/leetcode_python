#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 9:17
# @File    : heap_sort.py
# @author  : dfkai
# @Software: PyCharm
# 堆排序

# dataset = [16,9,21,3,13,14,23,6,4,11,3,15,99,8,22]
#
# for i in range(len(dataset)-1,0,-1):
#     print("-------",dataset[0:i+1],len(dataset),i)
#     #for index in range(int(len(dataset)/2),0,-1):
#     for index in range(int((i+1)/2),0,-1):
#         print(index)
#         p_index = index
#
#         l_child_index = p_index *2 - 1
#         r_child_index = p_index *2
#         print("l index",l_child_index,'r index',r_child_index)
#         p_node = dataset[p_index-1]
#         left_child =  dataset[l_child_index]
#
#         if p_node < left_child:  # switch p_node with  left child
#             dataset[p_index - 1], dataset[l_child_index] = left_child, p_node
#             # redefine p_node after the switch ,need call this val below
#             p_node = dataset[p_index - 1]
#
#         if r_child_index < len(dataset[0:i+1]): #avoid right out of list index range
#         #if r_child_index < len(dataset[0:i]): #avoid right out of list index range
#             #print(left_child)
#             right_child =  dataset[r_child_index]
#             print(p_index,p_node,left_child,right_child)
#
#             # if p_node <  left_child: #switch p_node with  left child
#             #     dataset[p_index - 1] , dataset[l_child_index] = left_child,p_node
#             #     # redefine p_node after the switch ,need call this val below
#             #     p_node = dataset[p_index - 1]
#             #
#             if p_node < right_child: #swith p_node with right child
#                 dataset[p_index - 1] , dataset[r_child_index] = right_child,p_node
#                 # redefine p_node after the switch ,need call this val below
#                 p_node = dataset[p_index - 1]
#
#         else:
#             print("p node [%s] has no right child" % p_node)
#
#
#     #最后这个列表的第一值就是最大堆的值，把这个最大值放到列表最后一个， 把神剩余的列表再调整为最大堆
#
#     print("switch i index", i, dataset[0], dataset[i] )
#     print("before switch",dataset[0:i+1])
#     dataset[0],dataset[i] = dataset[i],dataset[0]
#     print(dataset)
#
# # 人类能理解的版本

# [3,2,5,3,6]
def sift(li, low, high):
    tmp = li[low]
    i = low
    j = 2 * i + 1
    print(tmp,i,j)
    while j <= high:  # 退出条件2：当前i位置是叶子结点，j位置超过了high
        # j 指向更大的孩子
        if j + 1 <= high and li[j + 1] > li[j]:
            j = j + 1  # 如果右孩子存在并且更大，j指向右孩子
        if tmp < li[j]:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:  # 退出条件1：tmp的值大于两个孩子的值
            break
    li[i] = tmp

def heap_sort(li):
    # 1. 建堆
    n = len(li) # 5
    for i in range(n // 2 - 1, -1, -1):
        print(i,n-1)
        # i 是建堆时要调整的子树的根的下标
        sift(li, i, n - 1)
    print("one done")
    # 2.挨个出数
    for i in range(n - 1, -1, -1):  # i表示当前的high值 也表示棋子的位置
        print(i)
        li[i], li[0] = li[0], li[i]
        # 现在堆的范围 0~i-1
        sift(li, 0, i - 1)
if __name__ == '__main__':
    li = [3,2,5,3,6]
    heap_sort(li)
    print(li)