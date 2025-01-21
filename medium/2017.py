from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        n = len(grid[0])
        prefixRow1, prefixRow2 = grid[0].copy(), grid[1].copy()
        
        for i in range(1, n):
            prefixRow1[i] += prefixRow1[i - 1]
            prefixRow2[i] += prefixRow2[i - 1]
        res = float("inf")

        for i in range(n):
            top = prefixRow1[-1] - prefixRow1[i]
            bottom = prefixRow2[i - 1] if i > 0 else 0
            second = max(top, bottom)
            res = min(res, second)
        return res      