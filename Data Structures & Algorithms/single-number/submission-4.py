class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsD = Counter(nums)

        for key,value in numsD.items():
            if value == 1:
                return key