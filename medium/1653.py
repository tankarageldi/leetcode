class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        delete = 0

        for char in s:
            if stack and stack[-1] == "b" and char == "a":
                stack.pop()
                delete += 1
            else:
                stack.append(char)
        return delete
            
            

sol = Solution()
s = "aababbab"
s1 = "bbaaaaabb"
print(sol.minimumDeletions(s))
print(sol.minimumDeletions(s1))