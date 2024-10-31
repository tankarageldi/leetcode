class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
                print(s[i])
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                times = ""
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                encoded = int(times) * substr
                stack.append(encoded)

        return "".join(stack)

sol = Solution()
s = "2[abc]3[cd]ef"
print(sol.decodeString(s))