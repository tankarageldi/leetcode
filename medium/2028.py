class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        res = (n + len(rolls)) * mean - sum(rolls)
        if res > 6 * n or res < n:
            return []
        dist = res // n
        mod = res % n

        result = [dist] * n
        for i in range(mod):
            result[i] += 1
        return result
        


rolls = [3,2,4,3]
mean = 4
n = 2
rolls1 = [1,5,6]
mean1 = 3
n1 = 4
sol = Solution()
print(sol.missingRolls(rolls,mean,n)) # [6,6]
print(sol.missingRolls(rolls1,mean1,n1)) # [2,3,2,2]
