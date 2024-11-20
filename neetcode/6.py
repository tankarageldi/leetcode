class Solution:
    def encode(self, strs: list[str]) -> str:
        ans = ""
        for i in range(len(strs)):
            if i == (len(strs) - 1):
                ans += strs[i]
            else: 
                ans += strs[i] + "!"
        return ans
        
    def decode(self, s: str) -> list[str]:
        if s == "":
            return ""
        if s == []:
            return []
        return s.split("!")

s = Solution()
strs= ["neet","code","love","you"]
x = s.encode(strs)
print(x)
print(s.decode(x))