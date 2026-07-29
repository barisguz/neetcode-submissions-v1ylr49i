class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        my_dict = {}

        for i in nums: 
            my_dict[i] = my_dict.get(i,0) + 1
        
        ## duplicate check 
        for values in my_dict.values(): 
            if values % 2 == 1: 
                return False
        return True