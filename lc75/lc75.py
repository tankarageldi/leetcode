


class Solution:
    # 1 
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n = len(word1),len(word2)
        res = ""
        i,j = 0,0

        while i < m or j <n:
            if i < m:
                res += word1[i]
                i = i + 1
            if j < n:
                res += word2[j]
                j = j + 1
        return res
        
    
    #2 
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        from math import gcd

        if str1 + str2 != str2 + str1: 
            return ""
        
        gcd = gcd(len(str1),len(str2))
        return str1[:gcd]
    #3
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        ans = []
        candies_length = len(candies)
        helper = sorted(candies)
        maxim = helper[candies_length - 1]
        
        for i in range(candies_length):
            if candies[i] + extraCandies < maxim:
                ans.append(False)
            else:
                ans.append(True)
        return ans

    #4 sol 1
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if length < 2 and flowerbed[i] == 0:
                count += 1
            else:
                if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif i == length - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
        if count < n:
            return False
        else:
            return True
    #4 sol 2
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                check_left = (i == 0) or (flowerbed[i - 1] == 0)
                check_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                if check_left and check_right:
                    flowerbed[i] = 1
                    count += 1
        return count >= n

    #5 
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiuoAEUIO'
        word = list(s)
        end = len(s) - 1
        start = 0
        while end > start:
            while end > start and vowels.find(word[start]) == -1:
                start += 1
            while end > start and vowels.find(word[end]) == -1:
                end -= 1
            word[start], word[end] = word[end],word[start]
            start += 1
            end -= 1

            
                   
                   
        return ''.join(word)
                
