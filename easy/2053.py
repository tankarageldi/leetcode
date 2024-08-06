class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        dic = {}
        for str in arr:
            if str in dic:
                dic[str] += 1
            else:
                dic[str] = 1
        for key,value in dict(dic).items():
            if value > 1:
                del dic[key]
        l = list(dic.keys())
        if k <= len(l):
            return l[k-1]
        
        return ""
        
sol = Solution()
arr = ["d","b","c","b","c","a"]
k = 2
arr1 = ["aaa","aa","a"]
k1 = 1 
arr2 = ["a","b","a"] 
k2 = 3
print(sol.kthDistinct(arr,k))
print(sol.kthDistinct(arr1,k1))
print(sol.kthDistinct(arr2,k2))