class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_arr = [1] *  len(nums)
        suffix_arr = [1] * len(nums)

        for i in range(1,len(nums)):
            prefix_arr[i] = prefix_arr[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_arr[i] = suffix_arr[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = suffix_arr[i] * prefix_arr[i]

        return nums

sol = Solution()
nums = [1,2,4,6]
print(sol.productExceptSelf(nums))


