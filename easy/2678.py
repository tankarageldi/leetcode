class Solution:
    def countSeniors(self, details: list[str]) -> int:
        valid = 0
        for i in range(len(details)):
            s = details[i]
            if int(s[11] + s[12]) > 60:
                valid += 1
        return valid
    
sol = Solution()
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
details1 = ["1313579440F2036","2921522980M5644"]
print(sol.countSeniors(details=details))
print(sol.countSeniors(details=details1))

        