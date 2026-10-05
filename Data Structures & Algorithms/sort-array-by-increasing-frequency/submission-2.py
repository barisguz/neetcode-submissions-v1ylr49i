class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        numCount = Counter(nums)

        nums.sort(key=lambda n: (numCount[n],-n))
        return nums