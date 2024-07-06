class Solution:
       def pivotIndex(self, nums: list[int]) -> int:
        left_sum = nums[0]
        right_sum = sum(nums)
        if right_sum - left_sum == 0: 
            return 0
        right_sum -= nums[0]
        for i in range(1,len(nums)):
            right_sum -= nums[i]
            if left_sum != right_sum:
                left_sum += nums[i]
            else:
                return i
        return -1
