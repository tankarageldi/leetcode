class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        t = {}
        for num in (nums):
            if num in t:
                t[num] +=1
            else:
                t[num] = 1
        nums.sort(key=lambda x: (t[x],-x))
        return nums
sol = Solution()
nums1 = [1,1,2,2,2,3]
nums2 = [2,3,1,3,2]
nums3 = [-1,1,-6,4,5,-6,1,4,1]
print(sol.frequencySort(nums=nums1))
print(sol.frequencySort(nums=nums2))
print(sol.frequencySort(nums=nums3))