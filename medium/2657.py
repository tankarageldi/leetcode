from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        pref = []
        seen = [False] * (n + 1)
        common = 0
        
        for i in range(n):
            if not seen[A[i]]:
                seen[A[i]] = True
            elif seen[A[i]]:
                common += 1
            if not seen[B[i]]:
                seen[B[i]] = 1
            elif seen[B[i]]:
                common += 1
            pref.append(common)
        return pref
    
sol = Solution()
A = [1,3,2,4]
B = [3,1,2,4]
print(sol.findThePrefixCommonArray(A,B))


