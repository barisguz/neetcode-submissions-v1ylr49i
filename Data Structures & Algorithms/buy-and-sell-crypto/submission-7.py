class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0 
        minBuy = prices[0]

        for sellP in prices: 
            maxP = max(maxP, sellP - minBuy)
            minBuy = min(sellP, minBuy)
        return maxP