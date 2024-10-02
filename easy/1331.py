class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        copy = sorted(arr)
        table = {}
        counter = 1
        for element in copy:
            if element in table:
                continue
            else:
                table[element] = counter
                counter+=1
            
        for i in range(len(arr)):
            arr[i] = table[arr[i]]
        
        return arr
sol = Solution()
arr = [40,10,20,30]
arr1 = [100,100,100]
arr2 = [37,12,28,9,100,56,80,5,12]
print(sol.arrayRankTransform(arr))
print(sol.arrayRankTransform(arr1))
print(sol.arrayRankTransform(arr2))