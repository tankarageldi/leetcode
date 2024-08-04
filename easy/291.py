class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in dic and abs(dic[curr] - i) <= k:
                return True
            else:
                dic[curr] = i
        return False
        
    

sol = Solution()
nums = [1,2,3,1,2,3]
k = 2
nums1 = [1,2,3,1]
k1 = 3
print(sol.containsNearbyDuplicate(nums,k))
print(sol.containsNearbyDuplicate(nums1,k1))