class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numDict = Counter(nums)
        firstNum = -1
        setNums = set()

        ## [1,2,3,6,5]
        for i in range(len(nums)):
            setNums.add(i+1)

        for key,value in numDict.items():
            if value == 2: 
                firstNum = key
            setNums.remove(key)
        return [firstNum, setNums.pop()]
            

        
