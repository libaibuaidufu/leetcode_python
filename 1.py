#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 0027 10:50
# @File    : 1.py
# @author  : dfkai
# @Software: PyCharm
"""
question:
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
    示例:
        给定 nums = [2, 7, 11, 15], target = 9
        因为 nums[0] + nums[1] = 2 + 7 = 9
        所以返回 [0, 1]
think:
    判断减数是否在 剩余的nums 中 ，然后索引。
"""
# python3
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, key in enumerate(nums):
            if (target - key) in nums[index + 1:]:
                return [nums.index(key), nums[index + 1:].index(target - key) + index + 1]


if __name__ == '__main__':
    s = Solution()
    data = s.twoSum([3, 2, 4], target=6)
    print(data)
