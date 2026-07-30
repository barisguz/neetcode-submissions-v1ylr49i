class Solution:
    def maxDifference(self, s: str) -> int:
        ## iterate through, put their occurances in a dict 
        ## and then sort that dict, start from the end first and find the largest even
        ## and then go back to beginning and find the smallest odd
        ## return the diff 

        my_dict = {}
        lowest = 0
        largest = 0

        for i in s: 
            my_dict[i] = my_dict.get(i,0) + 1
        sorted_dict = dict(sorted(my_dict.items(),key=lambda x: x[1]))

        for key in sorted_dict: 
            if (sorted_dict[key] % 2 == 0):
                lowest = key
                break
        for key in reversed(sorted_dict): 
            if (sorted_dict[key] % 2 == 1): 
                largest = key
                break
        return sorted_dict[largest] - sorted_dict[lowest]