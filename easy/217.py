class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
        # return False
        dic = {}
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1
        return False
        
sol = Solution()
nums = [1,2,3,1]
nums1 = [1,2,3,4]
nums2 = [1,1,1,3,3,4,3,2,4,2]
print(sol.containsDuplicate(nums=nums))
print(sol.containsDuplicate(nums=nums1))
print(sol.containsDuplicate(nums=nums2))