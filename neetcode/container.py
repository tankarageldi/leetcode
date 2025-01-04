class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i = 0 
        j = len(heights) - 1
        max_Area = 0
        while i < j:
            curr = min(heights[i],heights[j]) * (j - i)
            max_Area = max(curr,max_Area)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_Area
            
        

sol = Solution()
height = [1,7,2,5,4,7,3,6]
print(sol.maxArea(height))
