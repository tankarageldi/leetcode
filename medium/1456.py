class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        count = 0
        left = 0
        result = 0
        for i in range(len(s)):
            count += 1 if s[i] in vowels else 0
            if i - left + 1 > k:
                cnt -= 1 if s[left] in vowels else 0
                left += 1
            res = max(res,count)
        return res
    
sol = Solution()
s1 = "weallloveyou" 
k1 = 7
print(sol.maxVowels(s1,k1))





