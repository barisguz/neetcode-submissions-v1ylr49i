class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        rows = 0 
        i = 1
        length = n

        while i < length:
            length = length - i
            rows += 1
            i += 1

        return rows
