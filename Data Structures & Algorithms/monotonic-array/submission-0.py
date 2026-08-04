class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        isIncreasing = False
        isDecreasing = False

        if (nums[0] > nums[len(nums) -1]):
            isDecreasing = True
        else:
            isIncreasing = True


        for i in range(1,len(nums)):
            if (nums[i] > nums[i-1] and isDecreasing):
                return False
            elif (nums[i] < nums[i-1] and isIncreasing):
                return False
        return True

