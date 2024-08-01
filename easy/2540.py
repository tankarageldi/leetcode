class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i=0
        j=0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i+=1 
            elif nums2[j] < nums1[i]:
                j+= 1
            else:
                return nums1[i]
        return -1 
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        common = list(set(nums1).intersection(nums2))
        if common:
            common.sort()
            return common[0]
        return -1
        
sol = Solution()
nums1 = [1,2,8,12,32,34,43,52,57,62,64,67,71,71,79,81,86,91,93,94]
nums2 = [9,11,12,14,19,25,29,31,38,39,41,42,58,63,66,70,71,73,91,91]
print(sol.getCommon(nums1,nums2))
