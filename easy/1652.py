class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        result = [0] * len(code)
        if k == 0 :
            return result
        
        for i in range(len(result)):
            if k > 0:
                for j in range(i+1,i+k+1):
                    result[i] += code[j % len(code)]
            else:
                for j in range(i - abs(k),i):
                   result[i] += code[(j + 100*len(code)) % len(code)]
        return result
        

sol = Solution()
code = [5,7,1,4]
code1 = [1,2,3,4]
code2 = [2,4,9,3]
k = 3
k1 = 0
k2 = -2
print(sol.decrypt(code,k))
print(sol.decrypt(code1,k1))
print(sol.decrypt(code2,k2))