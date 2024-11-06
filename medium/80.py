class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dic = {}
        loop = True
        for element in nums:
            if element in dic: 
                dic[element] += 1
            else:
                dic[element] = 1 
        for key,value in dic.items():
            while value > 2: 
                i = nums.index(key)
                nums.remove(nums[i])
                value = value - 1
        return len(nums)



sol = Solution()
nums = [1,1,1,2,2,3]
nums1 = [0,0,1,1,1,1,2,3,3]

print(sol.removeDuplicates(nums))
print(sol.removeDuplicates(nums1))