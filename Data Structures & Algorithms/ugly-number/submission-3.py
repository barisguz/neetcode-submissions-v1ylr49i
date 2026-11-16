class Solution:
    def isUgly(self, n: int) -> bool:
        ## make a while loop and check if the given number is 

        ## divisible by 2,3, or 5. if it is, divide it and move on
        ## at the end, if the number that is left is not 1, return false take the absolute value of it

        if n < 0: 
            return False

        while (n % 2 == 0):
            n = n /2
        while (n % 3 == 0):
            n = n /3
        while (n % 5 == 0):
            n = n /5
        if (n == 1):
            return True
        return False