class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1
        return len(set(dic.values())) == len(dic)

sol = Solution()
arr = [1,2,2,1,1,3]
arr1 = [1,2]
print(sol.uniqueOccurrences(arr=arr))
print(sol.uniqueOccurrences(arr=arr1))
            