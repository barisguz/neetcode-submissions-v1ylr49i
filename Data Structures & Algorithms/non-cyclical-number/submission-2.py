class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while True:
            result = self.intTotal(n)
            if (result == 1):
                return True
            if (result in seen): 
                return False
            seen.add(result)
            n = result

    def intTotal(self, num: int)  -> int:
        digits = [int(d) for d in str(abs(num))]
        total = 0 
        for i in digits: 
            total += i * i
        return total

