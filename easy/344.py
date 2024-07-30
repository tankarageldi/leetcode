
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        print(s)
        
sol = Solution()
s = ["h","e","l","l","o"]
s1 = ["H","a","n","n","a","h"]
sol.reverseString(s=s)
sol.reverseString(s=s1)
