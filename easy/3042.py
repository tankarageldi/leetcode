from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str,str2: str):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            else:
                return False
        total = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    total += 1
        
        return total

sol = Solution()
words = ["bb","bb"]
words1 = ["a","aba","ababa","aa"]
words2 = ["pa","papa","ma","mama"]
words3 = ["abab","ab"]
print(sol.countPrefixSuffixPairs(words))
print(sol.countPrefixSuffixPairs(words1))
print(sol.countPrefixSuffixPairs(words2))
print(sol.countPrefixSuffixPairs(words3))