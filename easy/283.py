class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        length = len(nums)
        for right in range (length):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

            
