class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
 ##Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
 ##                i                        j
##Output: [22,28,8,6,17,44]
##      Counter for arr1 
## for counter numbers, go through arr2 and put them in that order and reset the values to 0 after, 
## and then go through the counter map again and add the rest of the non zero ones in an ascending order 

        count = Counter(arr1)
        latestNums = []
        remainingChars = []

        for num in arr2:
            
            latestNums.extend([num] * count[num])
            count[num] = 0
        
        for key in count: 
            if count[key] > 0:
                remainingChars.extend([key] * count[key])
                count[key] = 0

        remainingChars.sort()
        latestNums.extend(remainingChars)

        return latestNums
