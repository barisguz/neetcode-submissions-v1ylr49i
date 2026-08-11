class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ## bills dictionary {5:0 , 10:1, 20:2}
        billsDic = {5: 0, 10: 0, 20: 0} 
        for i in bills: 
            if (i == 5):
                billsDic[5] += 1
            elif (i == 10): 
                if billsDic[5] == 0:
                    return False
                billsDic[10] += 1
                billsDic[5] -= 1
            else:
                if (billsDic[10] >= 1 and billsDic[5] >= 1):
                    billsDic[10] -= 1
                    billsDic[5] -= 1
                    billsDic[20] += 1
                elif(billsDic[5] > 2):
                    billsDic[5] = billsDic[5] - 2
                    billsDic[20] += 1
                else:
                    return False
        return True

                