"""
小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？

输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。

示例 1：

输入：guess = [1,2,3], answer = [1,2,3]
输出：3
解释：小A 每次都猜对了。

链接：https://leetcode-cn.com/problems/guess-numbers
"""
from typing import List
class Solution:
    def game_on(self, guess: List[int], answer: List[int]) -> int:
        if guess == answer:
            return 3
        num = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                num+=1
        return num
    
    def game_two(self, guess: List[int], answer: List[int]) -> int:
        if guess == answer:
            return 3
        num = len(list(filter(lambda x:guess[x]==answer[x],range(3))))
        return num
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum(map(lambda x, y: x == y, guess, answer))
if __name__ == "__main__":
    so = Solution()
    data = so.game([1,2,3],[3,2,1])
    print(data)
            