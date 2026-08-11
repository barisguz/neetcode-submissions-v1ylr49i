class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        duplicate, missing = 0,0
        for i in range(1,len(nums) + 1):
            if freq[i] == 0:
                missing = i
            if freq[i] == 2:
                duplicate = i
        return [duplicate,missing]
