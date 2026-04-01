class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res = 0
        highest = 0

        i = 0
        j = len(heights) - 1
        while i < j:
            volume = (j-i) * min(heights[i],heights[j])
            highest = max(highest,volume)
            if heights[i] > heights[j]: 
                j -= 1
            else: 
                i += 1 
            
        return highest