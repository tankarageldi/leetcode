class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sen = sentence.split()
        for i in range(len(sen)):
            if sen[i].startswith(searchWord):
                return i + 1
        return -1

    

sol = Solution()
sentence = "i love eating burger"
searchWord = "burg"
print(sol.isPrefixOfWord(sentence,searchWord))