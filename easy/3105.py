from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxcnt_i = 1
        cnt_i = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cnt_i += 1
            else:
                maxcnt_i = max(cnt_i,maxcnt_i)
                cnt_i = 1
        maxcnt_i = max(cnt_i,maxcnt_i)
        maxcnt_d = 1
        cnt_d = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                cnt_d += 1
            else:
                maxcnt_d = max(maxcnt_d,cnt_d)
                cnt_d = 1
        maxcnt_d = max(maxcnt_d,cnt_d)
        return max(maxcnt_i,maxcnt_d)



sol = Solution()
nums = [1,4,3,3,2]
nums1 = [3,3,3,3]
nums2 = [3,2,1]
print(sol.longestMonotonicSubarray(nums))
print(sol.longestMonotonicSubarray(nums1))
print(sol.longestMonotonicSubarray(nums2))