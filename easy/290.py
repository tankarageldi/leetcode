class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()

        return len(l) == len(pattern) and len(set(l)) == len(set(pattern))
        

            


sol = Solution()
pattern ="abba"
s ="dog dog dog dog"
pattern1 = "abba"
s1 = "dog cat cat dog"
pattern2 = "aba"
s2 ="dog cat cat"
print(sol.wordPattern(pattern,s))
print(sol.wordPattern(pattern1,s1))
print(sol.wordPattern(pattern2,s2))
