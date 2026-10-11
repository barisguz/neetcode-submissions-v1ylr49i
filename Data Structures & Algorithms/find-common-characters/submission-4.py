class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # iterate through words and put the counter of letters into a dictionary 
        # go through letters with the count that is equal to the length of the size of the words array
        # return those letters 

        cnt = Counter(words[0])

        for i in words:
            cntCurr = Counter(i)
            for j in cnt:
                cnt[j] = min(cntCurr[j],cnt[j])
        res = []
        for i in cnt: 
            for j in range(cnt[i]):
                res.append(i)
        return res


