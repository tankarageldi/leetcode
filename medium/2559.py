from typing import List


class Solution:
    # def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    #     ans = [0] * len(queries)
    #     vowels = ['a','e','o','u','i']
    #     for j in range(len(queries)):
    #         query = queries[j]
    #         for i in range(query[0],query[1]+1):
    #             if words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels:
    #                 ans[j] += 1
    #     return ans
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = ['a','e','o','u','i']
        pref = [0] * len(words)
        ans = [0] * len(queries)
        sum = 0
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[len(word) - 1] in vowels:
                sum += 1
            pref[i] = sum
        for j in range(len(queries)):
            curr = queries[j]
            if curr[0] == 0:
                ans[j] = pref[curr[1]]
            else:
                ## learn the prefix sum calculations of intervals.
                ans[j] = pref[curr[1]] - pref[curr[0] - 1]
        
        return ans

        
sol = Solution()
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
words1 = ["a","e","i"]
queries1 = [[0,2],[0,1],[2,2]]
print(sol.vowelStrings(words,queries))
print(sol.vowelStrings(words1,queries1))
