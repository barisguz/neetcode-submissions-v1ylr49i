class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        totalCount = 0 
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                j += 1
                totalCount += 1
            i += 1 
        return totalCount


