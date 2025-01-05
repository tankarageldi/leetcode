from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for char in numbers:
            if char not in d:
                d[char] = target - char
        
        for i in range(len(numbers)):
            if (d[numbers[i]] in numbers) and i < numbers.index(d[numbers[i]]):
                return [i+1,numbers.index(d[numbers[i]])+1]
        return None
        

sol= Solution()
numbers = [1,2,3,4]
target = 3

print(sol.twoSum(numbers,target))