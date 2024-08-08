class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if not char == '*':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return "".join(stack)
       
sol = Solution()

s1 = "*****"
print(sol.removeStars(s=s1))
