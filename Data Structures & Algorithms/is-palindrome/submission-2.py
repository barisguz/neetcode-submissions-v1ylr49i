class Solution:
    def isPalindrome(self, s: str) -> bool:

        otherStr = ""

        for i in s: 
            if i.isalnum():
                otherStr += i.lower()
        return otherStr == otherStr[::-1]