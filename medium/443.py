class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group = 1
            while(i + group < len(chars) and chars[i + group] == chars[i]):
                group += 1
            chars[res] = chars[i]
            res += 1
            if group > 1:
                str_rep = str(group)
                chars[res:res+len(str_rep)] = list(str_rep)
                res += len(str_rep)
            i += group
        return res





sol = Solution()
chars = ["a","a","b","b","c","c","c"]
chars1 = ["a"]
chars2= ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(sol.compress(chars=chars))
print(sol.compress(chars=chars1))
print(sol.compress(chars=chars2))
      