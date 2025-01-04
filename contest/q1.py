class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        i = 0 
        left = ""
        right = ""

        while p[i] != "*":
            left = left + p[i]
            i += 1
        i += 1
        while len(p) > i:
            right = right + p[i]
            i += 1

        leftind = s.find(left)
        if leftind == -1:
            return False
        
        startofright = leftind + len(left)

        return s[startofright:].find(right) != -1
        
                





sol = Solution()
s = "luck"
p = "u*"
print(sol.hasMatch(s,p))