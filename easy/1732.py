class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix = []
        prefix.append(0)
        n = len(gain)
        for i in range(1,n+1):
            prefix.append(prefix[i-1] + gain[i-1])
        return max(prefix)

