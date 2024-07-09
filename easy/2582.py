import math


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        full_round = time // (n-1)
        extra = time % (n-1)

        if full_round % 2 == 0:
            return extra + 1
        else: 
            return n - extra

        
sol = Solution
n = 18
time = 38
print(sol.passThePillow(1,18,38))
