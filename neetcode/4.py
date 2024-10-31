class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = [[]]
        strs.sort()
        for i in range(len(strs)):
            same = [strs[i]]
            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    if strs[i] not in result and strs[j] not in result:
                        same.append(strs[j])
            result.append(same)
        return result



        

sol = Solution()
strs = ["act","pots","tops","cat","stop","hat"] # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(sol.groupAnagrams(strs))
