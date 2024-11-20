class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        if arr == sorted(arr):
            return (len(arr))
        
        stack = []
        prev = list[0]
        stack.append(prev)
        for i in range(len(arr)):
            if prev <= arr[i]:
                stack.append(arr[i])
                prev = arr[i]
            else:





sol = Solution()
arr = [1,2,3,10,4,2,3,5]
print(sol.findLengthOfShortestSubarray(arr))