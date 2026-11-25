class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        limit = len(nums) / 2

        seenMap = {}

        for i in nums: 
            if i in seenMap: 
                seenMap[i] += 1
            else:
                seenMap[i] = 1
                
            if seenMap[i] > limit:
                return i
        return 0
            