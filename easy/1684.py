class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_chars = set(allowed)
        consistent = 0

        for word in words:
            if all(char in allowed_chars for char in word):
                consistent+=1
        return consistent
sol = Solution()
allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]
allowed2 = "abc" 
words2 = ["a","b","c","ab","ac","bc","abc"]
allowed3 = "cad" 
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]
print(sol.countConsistentStrings(allowed=allowed1,words=words1))
print(sol.countConsistentStrings(allowed=allowed2,words=words2))
print(sol.countConsistentStrings(allowed=allowed3,words=words3))