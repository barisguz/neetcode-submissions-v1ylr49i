class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ## start with two pointer 
        ## Input: nums = [10,20,30,5,10,50] AND total = 0 
        ##               i-1
        ##                   i 
        ##

        currSum = nums[0]
        totalSum = nums[0]
        for i in range(1, len(nums)): 
            if (nums[i] > nums[i-1]): 
                currSum += nums[i]
            else: 
                currSum = nums[i]
            totalSum = max(totalSum, currSum)
        return totalSum


            
            





