class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        
        inversions = 0
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                inversions += 1

        if nums[0] < nums[n-1]:
            inversions += 1
        return inversions <= 1
    
sol = Solution()
nums = [3,4,5,1,2]
print(sol.check(nums))