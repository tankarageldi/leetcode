from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return [dic[diff],i]
            dic[n] = i

sol = Solution()
nums = [3,4,5,6]
target = 7
print(sol.twoSum(nums,target))
            
        