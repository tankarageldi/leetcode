class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        min_swaps = float("inf")
        total = sum(nums)
        count = nums[0]
        end = 0

        for start in range(len(nums)):
            if start != 0:
                count -= nums[start - 1]
            while end - start + 1 < total:
                end += 1
                count += nums[end % len(nums)]
            min_swaps = min(min_swaps,total - count)
        return min_swaps



        
    
sol= Solution()

nums11 = [1]

print(sol.minSwaps(nums=nums11))
