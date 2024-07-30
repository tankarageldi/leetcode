class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        a = list(s1.difference(s2))
        b = list(s2.difference(s1))
        return a,b
sol = Solution()
nums11 = [1,2,3]
nums22 = [2,4,6]
nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print(sol.findDifference(nums1,nums2))
print(sol.findDifference(nums11,nums22))