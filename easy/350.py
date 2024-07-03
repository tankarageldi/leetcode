class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        i,j = 0,0
        res = []
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            if nums1[i] > nums2[j]:
                j += 1
            else: 
                res.append(nums2[j])
                i += 1
                j += 1
        return res


            
                

sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
ans = sol.intersect(nums1,nums2)
print(ans)