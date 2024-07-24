class Solution:
    # Failed testcase 48, since deleting the duplicate values in the dictionary.
    # def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
    #     n = len(nums)
    #     arr=[None] * n
    #     d = {}
    #     for i in range(n):
    #         s = str(nums[i])
    #         element = ""
    #         for j in range(len(s)):
    #             digit =s[j]
    #             digit = int(digit)
    #             element += str(mapping[digit])
    #         arr[i] = int(element)
    #         d[nums[i]] = arr[i]
    #     list.sort(arr)
    #     x = 0
    #     for element in arr: 
    #         found = None
    #         for key,value in d.items():
    #             if value == element:
    #                 found = key
    #                 break
            
    #         if found is not None:
    #             nums[x] = found
    #             x += 1 
    #             del d[found]
    #         else:
    #             nums[x] = element
    #             x += 1
    #     return nums
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        pairs = []
        n = len(nums)
        for i in range(n):
                s = str(nums[i])
                element = ""
                for j in range(len(s)):
                    digit =s[j]
                    digit = int(digit)
                    element += str(mapping[digit])
                value = int(element)
                pairs.append((value,i))
        pairs.sort()
        arr = []
        for pair in pairs:
             arr.append(nums[pair[1]])
        return arr


            



sol = Solution()
mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]
sol.sortJumbled(mapping=mapping,nums=nums)
