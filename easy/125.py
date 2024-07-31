import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]
        

sol= Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s=s))