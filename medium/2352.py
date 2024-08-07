class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        cols = []
        rows = []
        ans = 0
        for i in range(len(grid)):
            col = []
            for j in range(len(grid[i])):
                col.append(grid[j][i])
            cols.append(col)
            rows.append(grid[i])
        for col in cols:
            for row in rows:
                if col == row:
                    ans += 1
        return ans
    
sol = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
grid1 = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(sol.equalPairs(grid=grid))
print(sol.equalPairs(grid=grid1))


