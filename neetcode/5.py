class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        res = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        for key,value in sorted_dict.items():
            if k > 0:
                res.append(key)
                k-=1
        return res

nums = [1,1,2,2,2,2,3]
k = 2
nums1 = [1,2]
k1 = 2



sol = Solution()
print(sol.topKFrequent(nums,k))
print(sol.topKFrequent(nums1,k1))
