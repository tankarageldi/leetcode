class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]