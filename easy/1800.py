class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = 0
        curr = 0
        
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(1,n):
            if nums[i-1] < nums[i]:  
                curr += nums[i-1]
            else:
                curr += nums[i-1]
                max_sum = max(max_sum,curr)
                curr = 0
        
        if nums[n -2] < nums[n-1]:
            curr += nums[n-1]
        max_sum = max(max_sum,curr)

        return max_sum

                
nums = [12,17,15,13,10,11,12]
sol = Solution()
print(sol.maxAscendingSum(nums))