class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for x in strs:
            res += str(len(x)) + "#" + x
        return res
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            res.append(s[j + 1 : j + 1 + l])
            i = j + 1 + l
        return res

            



       

s = Solution()
strs= ["neet","code","love","you"]
x = s.encode(strs)
print(x)
a = s.decode(x)
print(a)