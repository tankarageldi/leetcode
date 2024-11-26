class Solution:
    def longestConsecutive(self,nums: list[int]) -> int:
        nums.sort()
        curr = 1
        longest = 1
        if not nums:
            return 0
        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                longest = max(longest,curr)
                curr = 1
        return max(longest,curr)

sol = Solution()
nums = [2,20,4,10,3,4,5]
nums2=[9,1,4,7,3,-1,0,5,8,-1,6]
print(sol.longestConsecutive(nums))
print(sol.longestConsecutive(nums2))

