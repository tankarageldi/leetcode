class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        res_str = ''
        for char in s:
            curr = str(alphabet.index(char) + 1) 
            res_str += curr
        it = str(res_str)
        while k > 0:
            res = 0
            for char in it: 
                res += int(char)
            it = str(res)
            k -= 1
        return int(it)

s = "leetcode"
k = 2

sol=Solution()
print(sol.getLucky(s,k))