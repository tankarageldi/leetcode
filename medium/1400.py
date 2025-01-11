class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        d =  {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        odd_count = 0
        even_count = 0
        for key,value in d.items():
            if value % 2 == 1:
                odd_count += 1
            else:
                even_count += 1
        if odd_count > k:
            return False
        
        return True

sol = Solution()
s = "annabelle"
k = 2
print(sol.canConstruct(s,k))
