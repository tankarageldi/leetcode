class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in dic:
                return [i,dic[c]]
            
            dic[nums[i]] = i