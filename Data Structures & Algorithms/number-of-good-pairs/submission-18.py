class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        

        numCount = Counter(nums)
        totalC = 0
        for k in numCount:
            if numCount[k] > 1:
                localCount = numCount[k]

                totalC = totalC + (localCount * (localCount - 1)) / 2
        return int(totalC)