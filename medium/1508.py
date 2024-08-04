class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sums_arr=[]
        prev = 0
        elements = 0
        for i in range(n):
            for j in range(i,n):
                if j == i:
                    sums_arr.append(nums[j])
                    elements += 1
                else:
                    sums_arr.append(nums[j] + sums_arr[elements - 1])
                    elements += 1
            
        sums_arr.sort()
        sum_ = 0
        mod = 10**9 + 7
        for i in range(left -1, right):
            sum_ = (sum_ + sums_arr[i]) % mod 
        return sum_
    
sol = Solution()
nums = [1,2,3,4]
n = 4
left = 3
right = 4
print(sol.rangeSum(nums,n,left,right))
