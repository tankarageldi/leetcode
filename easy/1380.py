class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        min_row = []
        max_col = []
        checklist = []
        for row in matrix:
            min_row.append(min(row))
        for i in range(m):
            for j in range(n):
                checklist.append(matrix[j][i])
            max_col.append(max(checklist))
            checklist.clear()
        for element1 in min_row:
            for element2 in max_col:
                if element1 == element2:
                    checklist.append(element1)
        return checklist
                


sol = Solution()
matrix = [[3,7,8],
          [9,11,13],
          [15,16,17]]
matrix1 = [[7,8],
           [1,2]]
list = sol.luckyNumbers(matrix=matrix1)
print(list)
