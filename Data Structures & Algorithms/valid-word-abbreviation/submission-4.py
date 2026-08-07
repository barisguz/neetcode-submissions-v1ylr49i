class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        ## Input: word = "internationalization", abbr = "i12iz4n"

        i, j = 0,0

        while i < len(word) and j < len(abbr): 

            if abbr[j] == '0':
                return False
            if (word[i] == abbr[j]):
                i+= 1
                j += 1
            elif(abbr[j].isalpha()):
                return False
            else:
                subLen = 0
                while j <len(abbr) and abbr[j].isdigit():
                    subLen = subLen * 10 + int(abbr[j])
                    j +=1 
                i += subLen
        return i == len(word) and j == len(abbr)