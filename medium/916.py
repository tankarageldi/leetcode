from collections import Counter, defaultdict
from typing import List


class Solution:
    # My initial solution
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []

        for i in range(len(words1)):
            count = 0
            for j in range(len(words2)):
                if words1[i].count(words2[j]) == 0:
                    break
                count += 1
            if count == len(words2):
                ans.append(words1[i])
        return ans
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count2 = defaultdict(int)

        for w in words2:
            count_w = Counter(w)

            for c,cnt in count_w.items():
                count2[c] = max(count2[c],cnt)

        res = []

        for w in words1:
            count_w = Counter(w)
            flag = True
            for c,cnt in count2.items():
                if count_w[c] < cnt:
                    flag = False
                    break
            if flag:
                res.append(w)
        return res

        



    
sol = Solution()
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

words11 = ["amazon","apple","facebook","google","leetcode"]
words21 = ["l","e"]

words12 = ["amazon","apple","facebook","google","leetcode"]
words22 = ["lo","eo"]
print(sol.wordSubsets(words1,words2))
print(sol.wordSubsets(words11,words21))
print(sol.wordSubsets(words12,words21))

                       