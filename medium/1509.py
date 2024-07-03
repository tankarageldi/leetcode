class Solution:
    def minDifference(self, nums: list[int]) -> int:
        nums_size = len(nums)
        if nums_size <= 4:
            return 0
        nums.sort()
        minDiff = float("inf")
        for left in range(4):
            right = nums_size - 4 + left
            minDiff = min(minDiff,nums[right] - nums[left])
        return minDiff


sol = Solution()
nums = [1,7,9,11,14,17,21,22]
ans = sol.minDifference(nums=nums)
print(ans)



            
        