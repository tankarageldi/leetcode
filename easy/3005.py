class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        dic={}
        max_val=0
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        values = list(dic.values())
        values.sort(reverse=True)
        prev = values[0]
        max_val += prev
        i = 1
        while i < len(values):
            if prev == values[i]:
                max_val += prev
                prev = values[i]
            i += 1
        return max_val


                


        

sol = Solution()
nums = [1,2,2,3,1,4]
nums1 = [1,2,3,4,5]
print(sol.maxFrequencyElements(nums=nums))
print(sol.maxFrequencyElements(nums=nums1))