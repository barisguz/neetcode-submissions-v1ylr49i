from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Map = Counter(s1)
        s2Map = Counter()

        window_size = len(s1)

        for i in range(len(s2)):

            s2Map[s2[i]] += 1
            if i >= window_size:
                if s2Map[s2[i - window_size]] == 1:
                    del s2Map[s2[i - window_size]]
                else:
                    s2Map[s2[i- window_size]] -=1 
            if s1Map == s2Map:
                return True
        return False



        # for i, n in enumerate(s1):
        #     s1Map[n] = i

        # while j < len(s2):
        #     if (s2[i:j])

        # if len(s1) > len(s2): return False 

        # s1Count, s2Count = [0] * 26, [0] * 26

        # for i in range(len(s1)):
        #     s1Count[ord(s1[i]) - ord('a')] += 1
        #     s2Count[ord(s1[i]) - ord('a')] += 1

        # matches = 0

        # for i in range(26):

        #     matches += (1 if s1Count[i] == s2Count[i] else 0)

        # l = 0 

        # for r in range (len(s1), len(s2)): 


            
            
