class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        output = [None] * (length-1)
        output.insert(0,1)
        r = 1

        for i in range(1,length):
            output[i] = nums[i-1] * output[i-1]

        for i in range(length-1,0,-1):
            output[i-1] = output[i-1] * nums[i] * r
            r = r * nums[i]
            
        return output

            
            

            
    
            



sol = Solution()
nums1 = [1,2,3,4] # [24,12,8,6]
nums2 = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums1))
print(sol.productExceptSelf(nums2))