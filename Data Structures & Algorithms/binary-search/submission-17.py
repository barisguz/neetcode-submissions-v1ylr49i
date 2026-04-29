class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i, j = 0, len(nums)-1

        ## i = 0, j = 5 

        ## [-1,0,2,4,6,8]
        ##   i     m   j

        while i <= j: 
            m = (i + j) // 2
            # print(f"Printing assigned m:{m} ")


            if(nums[m] < target): 
                ##temp = j 
                i = m + 1
                # print(f"First if statement hit i: {i}")
            elif(nums[m] > target): 
                j = m - 1
                # print(f"Second if statement hit j: {j}")
            elif(nums[m] == target):
                return m
        return -1