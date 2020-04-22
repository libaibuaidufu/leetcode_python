#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 22:15
# @File    : quick_sort.py
# @author  : dfkai
# @Software: PyCharm
# 快速排序 选取第一个数 作为 参考 设为 key 然后 第一个数的索引位 low 最高位的索引位 high
# 然后 while 判断当 最低位low 小于最高位 high 避免两者重合
# 然后 以 low索引 key 找出右边比他大的值 ，如果小于 则进行一次位置置换
# 然后 key 就被调位置 ，右边都是比他的 ，因为如果比他小 他们就行位置调换了
# 但是左边还有比他大 所以 再从左边找到 比key大的值调到 右边 进行位置置换
# 如此反复 就会得到 以key 为分割 左边都是比key小的 右边都是比key 大的值
# 然后再把左边的列表 放到程序中在执行一次 然后把右边的程序也在执行一次 如此循环

# def quick_sort(array, left, right):
#     '''
#
#     :param array:
#     :param left: 列表的第一个索引
#     :param right: 列表最后一个元素的索引
#     :return:
#     '''
#     if left >= right:
#         return
#     # 0 15
#     low = left
#     high = right
#     key = array[low]  # 第一个值
#     #     array = [96, 14, 10, 9, 6, 99, 16, 5, 1, 3, 2, 4, 1, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3, 22, 19, 2]
#     #     array = [2, 14, 10, 9, 6, 99, 16, 5, 1, 3, 2, 4, 1, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3, 22, 19, 96]
#     #     array = [2, 14, 10, 9, 6, 96, 16, 5, 1, 3, 2, 4, 1, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3, 22, 19, 99]
#     #     array = [8,4,1, 14, 6, 2, 3, 9,5, 13, 7,1, 8,10, 12]
#     print(low,high,key)
#     while low < high:  # 只要左右未遇见
#         while low < high and array[high] > key:  # 找到列表右边比key大的值 为止
#             high -= 1
#         # 此时直接 把key(array[low]) 跟 比它大的array[high]进行交换
#         array[low] = array[high]
#         array[high] = key
#         print(array,low,high,key)
#         while low < high and array[low] <= key:  # 找到key左边比key大的值，这里为何是<=而不是<呢？你要思考。。。
#             low += 1
#             # array[low] =
#         # 找到了左边比k大的值 ,把array[high](此时应该刚存成了key) 跟这个比key大的array[low]进行调换
#         array[high] = array[low]
#         array[low] = key
#         print(array,low,high,key)
#
#     quick_sort(array, left, low - 1)  # 最后用同样的方式对分出来的左边的小组进行同上的做法
#     quick_sort(array, low + 1, right)  # 用同样的方式对分出来的右边的小组进行同上的做法
#
#
# if __name__ == '__main__':
#     array = [96, 14, 10, 9, 6, 99, 16, 5, 1, 3, 2, 4, 1, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3, 22, 19, 2]
#     # array = [8,4,1, 14, 6, 2, 3, 9,5, 13, 7,1, 8,10, 12]
#     print("before sort:", array)
#     quick_sort(array, 0, len(array) - 1)
#
#     print("-------final -------")
#     print(array)


def part(li, left, right):  # 列表,最左索引,最右索引
    print(li[left:right+1])
    tmp = li[left]  # 先找个临时变量把第一个元素存起来
    while left < right:  # 当最左小于最右
        while left < right and li[right] >= tmp:  # 当最左<最右 且 最右边的值大于等于临时变量
            right -= 1  # 最右 往左 挪 1 个单位长度
        li[left] = li[right]  # 都不满足:把挪完之后的最右的值 赋值给 最左的值(即最右的值小于临时变量时,这个值挪到当前最左的值)
        while left < right and li[left] <= tmp:  # 当最左<最右 且 最左边的值小于等于临时变量
            left += 1  # 最左 往右 挪 1 个单位长度
        li[right] = li[left]  # 都不满足:把挪完之后的最左的值 赋值给 最右的值(即最左的值大于临时变量时,这个值挪到当前最右的值)
    li[left] = tmp  # 当前最左最右的值相等时,把这个值赋给临时变量
    print(left)
    return left  # 返回当前临时变量的索引


def quick(li, left, right):
    if left < right:  # 如果左索引<右索引
        mid = part(li, left, right)  # 调用part进行分区 返回一个索引赋给mid
        quick(li, left, mid - 1)  # 递归调用quick 直到left=mid-1
        quick(li, mid + 1, right)  # 递归调用quick 直到mid+1=right


# li = list(range(1000))
# import random
#
# random.shuffle(li)
# print(li)
# li = [96, 14, 10, 9, 6, 99, 16, 5, 1, 3, 2, 4, 1, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3, 22, 19, 2]
li = [3,5,2,3,6]
quick(li, 0, len(li) - 1)


#
# a = [1, 2, 3]
#
#
# def get(b):
#     b[1], b[0] = b[0], b[1]
#
#
# get(a)
# print(a)

# li = [3,5,2,3,6] 0 4 3
# li = [2,5,3,3,6] 0 2 3
# li = [2,3,5,3,6] 1 2 3
def quick_sort(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left
