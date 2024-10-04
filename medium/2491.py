class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        pair_sum = (sum(skill) / (len(skill)/2))
        ret = 0
        
        
        i = 0
        j = len(skill) - 1

        if skill[i] + skill[j] != pair_sum:
                return - 1
        while i < j:
            ret += skill[i]*skill[j]
            i+=1
            j-=1
        return ret




    
sol = Solution()
skill = [3,2,5,1,3,4]
skill1 = [3,4]
skill2 = [1,1,2,3]
skill3 = [2,2,2,2]
print(sol.dividePlayers(skill=skill))
print(sol.dividePlayers(skill=skill1))
print(sol.dividePlayers(skill=skill2))
print(sol.dividePlayers(skill=skill3))