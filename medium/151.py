class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        list_words = s.split()
        for item in reversed(list_words[1:]):
            res += item + " "
        last = list_words[0]
        res += last
        return res


        

sol = Solution()
s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"
print(sol.reverseWords(s1))
print(sol.reverseWords(s2))
print(sol.reverseWords(s3))