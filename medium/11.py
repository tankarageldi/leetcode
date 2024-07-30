class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(min(height[j],height[i]) * (j-i),max_area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area
sol = Solution()
height = [1,1]
height1 = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height=height))
print(sol.maxArea(height=height1))