class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # Start from the end of the array, make the first one -1,
        # and then the rest of the array startcontinuing and keep the local max, if the number is smaller than that, replace it with the local max 
        localMax = 0
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1: 
                localMax = arr[i]
                arr[i] = -1
            else: 
                if arr[i] < localMax:
                    arr[i] = localMax
                else:
                    temp = localMax
                    localMax = arr[i] 
                    arr[i] = temp

        return arr

             


        