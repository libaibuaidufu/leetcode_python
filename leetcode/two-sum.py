from typing import List


class Solution:
    def twoSum_one(self, nums: List[int], target: int) -> List[int]:
        for i_i, i in enumerate(nums):
            for z_i, z in enumerate(nums[i_i + 1:]):
                if i + z == target:
                    return [i_i, z_i + 1 + i_i]
        return []

    def twoSum_two(self, nums: List[int], target: int) -> List[int]:
        for i_i, i in enumerate(nums):
            z = target - i
            if z in nums[i_i + 1:]:
                z_i = nums[i_i + 1:].index(z)
                return [i_i, z_i + i_i + 1]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__ == "__main__":
    solution = Solution()
    data = solution.twoSum([2, 7, 11, 15], 9)
    print(data)
