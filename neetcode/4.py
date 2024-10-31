class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        appended = []
        for i in range(len(strs)):
            if strs[i] not in appended:
                curr = []
                curr.append(strs[i])
                appended.append(strs[i])
                for j in range(i+1,len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        curr.append(strs[j])
                        appended.append(strs[j])
                result.append(curr)
        return result



        

sol = Solution()
strs = ["",""]
strs1 = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs))
print(sol.groupAnagrams(strs1))
