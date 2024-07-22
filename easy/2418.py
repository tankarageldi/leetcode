class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        dictionary = dict(zip(heights,names))
        sorted_dic = {key: dictionary[key] for key in sorted(dictionary)}
        ans = sorted_dic.values()
        return list(reversed(ans))
        
        
sol = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]

names1 = ["Alice","Bob","Bob"]
heights1 = [155,185,150]
ans = sol.sortPeople(names,heights)
ans1 = sol.sortPeople(names1,heights1)

print(ans)
print(ans1)