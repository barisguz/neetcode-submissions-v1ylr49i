class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currMax = 0
        totalMax = 0
        
        for i in nums:
            if (i == 1): 
                currMax += 1
            else:
                currMax = 0 
            if currMax > totalMax: 
                totalMax = currMax
            
        return totalMax
