class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        my_dict = {}

        for i in nums: 
            my_dict[i] = my_dict.get(i,0) + 1
        
        ## duplicate check 
        for key in my_dict: 
            if my_dict[key] % 2 == 1: 
                return False
        return True