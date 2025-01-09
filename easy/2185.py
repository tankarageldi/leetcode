class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        ans = 0
        for word in words:
            ans += 1 if word.startswith(pref) else 0   
        return ans
    
words = ["pay","attention","practice","attend"]
pref = "at"
words1= ["leetcode","win","loops","success"]
pref1 = "code"
sol = Solution()
print(sol.prefixCount(words,pref))
print(sol.prefixCount(words1,pref1))