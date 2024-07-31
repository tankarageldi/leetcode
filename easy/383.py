class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for char in ransomNote:
            if char in dic:
                dic[char] += 1
            else: 
                dic[char] = 1
        for char in magazine: 
            if char in dic and dic[char] >= 0: 
                dic[char] -= 1
        for key in dic:
            if dic[key] > 0:
                return False
        return True
            

sol = Solution()
ransomNote = "aa"
magazine = "ab"
print(sol.canConstruct(ransomNote,magazine))