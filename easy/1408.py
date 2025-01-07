from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i].find(words[j]) != -1 and words[j] not in ans and words[i] != words[j]:
                    ans.append(words[j])
        return ans
    

sol = Solution()
words = ["mass","as","hero","superhero"]
print(sol.stringMatching(words))