class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        size = len(nums)
        ans = False
        first = float("inf")
        second = float("inf")

        for i in range(size):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second and nums[i] > first:
                second = nums[i]
            elif nums[i] > first and nums[i] > second:
                ans = True
        return ans
    

sol = Solution()
nums = [7,3,2,1,14,15]

print(sol.increasingTriplet(nums))
