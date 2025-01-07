class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        for i in range(len(s)):
            chars = []
            currlen = 0
            for j in range(i,len(s)):
                if s[j] in chars:
                    break
                else:
                    chars.append(s[j])
                    currlen += 1
            
            maxLen = max(currlen,maxLen)
        
        return maxLen

sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))