class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Input: prices = [10,1,5,6,7,1]
        ##                     i     i  
        ## maxProf = 0
        ## currProf = 0 
        ## Output: 6

        maxProf, currProf = 0,0 
        currNum = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < currNum:
                currNum = prices[i]
                continue
            elif prices[i] > currNum: 
                currProf = prices[i] - currNum
                maxProf = max(maxProf,currProf)

        return maxProf
             

