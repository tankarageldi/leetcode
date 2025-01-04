class Solution:
    ## better space comp
    def maxScore(self, s: str) -> int:
        max_score = 0
        for i in range(1,len(s)):
            left = s[:i].count("0")
            right = s[i:].count("1")
            max_score = max(max_score,left+right)
        return max_score
    
    ## better runtime 
    def maxScore(self, s: str) -> int:
        max_score = 0
        ones = s.count("1")
        zeros = 0

        for i in range(len(s)-1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
            max_score = max(max_score,ones+zeros)

        return max_score
        


sol = Solution()
s = "011101"
print(sol.maxScore(s))
