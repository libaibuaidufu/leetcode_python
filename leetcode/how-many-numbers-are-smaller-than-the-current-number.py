
# https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。

以数组形式返回答案。

示例 1：

输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。

"""
from typing import List 
class Solution:
    def smallerNumbersThanCurrent_one(self, nums: List[int]) -> List[int]:
        data = []
        for i in nums:
            data.append(len(list(filter(lambda x :x<i,nums))))
        return data
    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        data ={}
        n_nums = sorted(nums)
        for i_i,i in enumerate(sorted(nums)):
            if i_i-1>=0 and  i == n_nums[i_i-1]:
                data[i] = last
            else:
                data[i] = i_i
                last=i_i
        data_l= list(map(lambda x:data[x],nums))
        return data_l
    

if __name__ == "__main__":
    so = Solution()
    data = so.smallerNumbersThanCurrent([8,1,2,2,3])
    print(data)
