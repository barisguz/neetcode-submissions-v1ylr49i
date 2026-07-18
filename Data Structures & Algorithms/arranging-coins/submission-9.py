class Solution:
    def arrangeCoins(self, n: int) -> int:
        ## i = 0, i ++ when i > prev next 
        prev = 1
        totalCase = 0
        totalCount = n 
        
        if n == 1: 
            return 1
        while totalCount > prev: 
            totalCount = totalCount - prev 
            totalCase += 1
            prev += 1  

        return totalCase