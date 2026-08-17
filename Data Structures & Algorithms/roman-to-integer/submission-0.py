class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanMap = {"I": 1, "V":5, "X":10, "L":50,"C":100, "D":500, "M":1000}
        totalSum = 0

        ## VII
        
        for i in range(len(s)):
            if i < len(s) -1 and romanMap[s[i]] < romanMap[s[i+1]]:
                totalSum -= romanMap[s[i]]
            else:
                totalSum += romanMap[s[i]]
        return totalSum

        ## check if ascending? 