class Solution:
    # 0(N^2)
    def isSubsequence(self, s: str, t: str) -> bool:
        subs = ''
        j = 0
        for i in range(len(s)):
            while j < len(t):
                if t[j] == s[i]:
                    subs += s[i]
                    j += 1
                    break
                j += 1

        return subs == s
    # O(N)
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
