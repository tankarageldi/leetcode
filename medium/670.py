class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = [int(x) for x in str(num)]
        maxim = num
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                arr[i],arr[j] = arr[j],arr[i]
                comp = self.convert(arr)
                maxim = max(maxim,comp)
                arr[i],arr[j] = arr[j],arr[i]
        return maxim
    def convert(self,list):
        # Converting integer list to string list
        s = [str(i) for i in list]
        
        # Join list items using join()
        res = int("".join(s))
        
        return(res)

        

sol = Solution()
num = 98368
print(sol.maximumSwap(num))