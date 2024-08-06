import string
class Solution:
    def minimumPushes(self, word: str) -> int:
        alphabet = string.ascii_lowercase
        presses = 1
        dic={}
        for char in alphabet:
            if char =='s' or char == 'z':
                dic[char] = 4
                presses = 1
            elif presses > 3:
                presses = 1
                dic[char] = presses
                presses += 1
            else:
                dic[char] = presses
                presses += 1
        total = 0
        for char in word:
            
            total += dic[char]
        return total

sol = Solution()
word = "abcde" # 5
word1 = "xyzxyzxyzxyz" #12
word2 = "aabbccddeeffgghhiiiiii" # 24
print(sol.minimumPushes(word=word))
print(sol.minimumPushes(word=word1))
print(sol.minimumPushes(word=word2))