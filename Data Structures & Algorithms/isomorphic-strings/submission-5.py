class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {},{}

        for i in range(len(s)): 
            c1, c2 = s[i], t[i]

            if((c1 in tMap and tMap[c1] != c2) or (c2 in sMap and sMap[c2] != c1)):
                return False 
            
            sMap[c2] = c1
            tMap[c1] = c2
        return True
