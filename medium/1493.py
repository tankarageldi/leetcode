class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zero = 0
        max_window = 0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            
            while zero > 1:
                if nums[start] == 0:
                    zero -= 1
                start += 1
            max_window = max(max_window,i-start)
        return max_window
                       

    
sol = Solution()
nums = [1,1,0,1]
nums1 = [0,1,1,1,0,1,1,0,1]
nums2 = [1,1,1]
print(sol.longestSubarray(nums=nums))
print(sol.longestSubarray(nums=nums1))
print(sol.longestSubarray(nums=nums2))

            
                
            