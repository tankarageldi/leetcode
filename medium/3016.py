class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency list to store count of each letter
        frequency = [0] * 26

        # Count occurrences of each letter
        for c in word:
            frequency[ord(c) - ord("a")] += 1
        # Sort frequencies in descending order
        frequency.sort(reverse=True)

        total_pushes = 0

        # Calculate total number of presses
        for i in range(26):
            if frequency[i] == 0:
                break
            total_pushes += (i // 8 + 1) * frequency[i]

        return total_pushes

sol = Solution()
word = "abcde" # 5
word1 = "xyzxyzxyzxyz" #12
word2 = "aabbccddeeffgghhiiiiii" # 24
print(sol.minimumPushes(word=word))
print(sol.minimumPushes(word=word1))
print(sol.minimumPushes(word=word2))