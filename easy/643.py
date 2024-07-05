class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = 0
        n = len(nums)
        window_avg = sum(nums[:k])
        max_avg = window_avg

        for i in range(n-k):
            window_avg = (window_avg - nums[i] + nums[i + k])
            max_avg = max(window_avg, max_avg)
        return max_avg/k

sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(sol.findMaxAverage(nums=nums,k=k))