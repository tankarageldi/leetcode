from typing import List
from itertools import cycle
import string
circular_alphabet = cycle(string.ascii_lowercase)


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        diff_arr = [0] * n 

        for shift in shifts:
            start = shift[0]
            end = shift[1]
            dir = shift[2]

            if dir == 1:
                diff_arr[start] += 1
                if end + 1 < n:
                    diff_arr[end + 1] -= 1
            else:
                diff_arr[start] -= 1
                if end + 1 < n:
                    diff_arr[end + 1] += 1
            
        res = list(s)
        num = 0

        for i in range(n):
            num = ( num + diff_arr[i]) % 26
            if num < 0:
                num += 26
            
            shifted = chr(
                (ord(s[i]) - ord("a") + num) % 26 + ord("a")
            )
            res[i] = shifted
        return  "".join(res)

                

    # TIME LIMIT EXCEEDED, BUT WORKS

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alpha = list("abcdefghijklmnopqrstuvwxyz")
        charray = []
        ans = ''
        for element in s:
            charray.append(alpha.index(element))
        for array in shifts:
            start = array[0]
            end = array[1]
            dir = array[2]
            for i in range(start,end+1):
                if dir == 1:
                    charray[i] += 1
                else:
                    charray[i] -= 1
        for element in charray:
            ans += alpha[element + 26 % 26]
        return ans 




sol = Solution()
s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
s1 = "dztz"
shifts1 = [[0,0,0],[1,1,1]]
print(sol.shiftingLetters(s,shifts))
print(sol.shiftingLetters(s1,shifts1))