class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort()
        for num in nums:
            for item in nums[::-1]:
                if num + item == 0:
                    return item
        return -1
                
            
        
                
sol = Solution()
print(sol.findMaxK([-1, 2, -3, 3])) # -3