class Solution:
    # two pointers 
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and not nums1[i] in res:
                    res.append(nums1[i])

        return res
    
    # built in intersection operator for sets. 
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
res = sol.intersection(nums1,nums2)
print(res)