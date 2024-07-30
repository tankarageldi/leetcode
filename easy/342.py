import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log(n)/math.log(4)
        return x.is_integer()

sol = Solution()
print(sol.isPowerOfFour(16))
