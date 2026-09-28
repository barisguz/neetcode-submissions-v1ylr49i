class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        ## iterate through the list, on each word, go through other words  that are larger than that word to see if they exist in others, and then return the list at the end 
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
                    break
        return res  
