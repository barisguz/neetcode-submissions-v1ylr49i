class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        arrRev = arr
        arrRev.reverse()

        tempMax = arrRev[0]
        arrRev[0] = -1

        for i in range(1,len(arrRev)):
            if arrRev[i] > tempMax:
                temp = tempMax
                tempMax = arrRev[i]
                arrRev[i] = temp
            else:
                arrRev[i] = tempMax
        arrRev.reverse()
        return arrRev