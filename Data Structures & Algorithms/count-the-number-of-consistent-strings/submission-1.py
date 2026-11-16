class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0 

        allowedLetter = set(allowed)

        for word in words: 
            for letter in word: 
                if letter not in allowedLetter:
                    count -= 1
                    break
            count += 1 
        return count
                