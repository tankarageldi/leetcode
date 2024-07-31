class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
                right -= 1
                count += 1
        return count
sol = Solution()
nums = [1,2,3,4]
nums1 = [3,1,3,4,3]
k1 = 6
k = 5
print(sol.maxOperations(nums,k))
print(sol.maxOperations(nums1,k1))