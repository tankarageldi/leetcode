class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map1 = {}
        map2 = {}
        for char in word1:
            if char in map1:
                map1[char] += 1
            else:
                map1[char] = 1
        for char in word2:
            if char in map2:
                map2[char] += 1
            else:
                map2[char] = 1
        
        keys = set(map1.keys()) == set(map2.keys())
        map1 = sorted(map1.values()) 
        map2 = sorted(map2.values())
        return map1 == map2 and keys
       

         
sol = Solution()
word1 ="a"
word2 ="aa"
print(sol.closeStrings(word1,word2))
