class Solution:
    def minimumLength(self, s: str) -> int:
        freq={}

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        count = 0
        for value in freq.values():
            if value % 2 == 1:
                count += value - 1
            else:
                count += value - 2
                
                
        return len(s) - count
        


s = "abaacbcbb"
sol = Solution()
print(sol.minimumLength(s))
            
