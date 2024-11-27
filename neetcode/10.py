class Solution:
        def isPalindrome(self, s: str) -> bool:
            i = 0
            j = len(s) - 1
            s = s.lower()
            s.replace(" ", "")
            s = ''.join(ch for ch in s if ch.isalnum())
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True
