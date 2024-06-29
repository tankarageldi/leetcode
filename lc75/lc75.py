


class Solution:
    # 1 
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1),len(word2)
        res = ""
        i,j = 0,0

        while i < m or j <n:
            if i < m:
                res += word1[i]
                i = i + 1
            if j < n:
                res += word2[j]
                j = j + 1
        return res
        
    
    #2 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd

        if str1 + str2 != str2 + str1: 
            return ""
        
        gcd = gcd(len(str1),len(str2))
        return str1[:gcd]

sol = Solution()
str1 = "13579"
str2 = "2468"
ans = sol.mergeAlternately(str1,str2)
print(ans)