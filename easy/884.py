class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s = s1 + " " + s2 
        arr = s.split()
        res = []
        for word in arr:
            if arr.count(word) == 1:
                res.append(word)
        return res

        
        
sol = Solution()
s1 = "this apple is sweet"
s2 = "this apple is sour"
print(sol.uncommonFromSentences(s1,s2))
        