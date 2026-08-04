class Solution:
    def maxDepth(self, s: str) -> int:
        currDepth = 0
        totalDepth = 0

        for i in s:
            if (i == '('): 
                currDepth += 1
            elif (i == ')'):
                currDepth -= 1 
            totalDepth = max(totalDepth, currDepth)

        return totalDepth
            


