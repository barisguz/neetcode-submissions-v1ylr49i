class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ## create a set for both, for first iterate through second, for second iterate through first 

        set1 = set(nums1)
        set2 = set(nums2)
        res = [[],[]]
        for i in nums1: 
            if i not in set2 and i not in res[0]: 
                res[0].append(i)
        
        for i in nums2:
            if i not in set1 and i not in res[1]:
                res[1].append(i)

        return res