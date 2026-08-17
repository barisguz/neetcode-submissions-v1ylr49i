class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        numCounts = Counter(nums)
        totalCount = 0 

        for count in numCounts.values():
            totalCount += (count) * (count - 1) // 2
        return totalCount