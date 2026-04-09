class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        n = len(students)

        cnt = Counter(students)

        for s in sandwiches: 
            if cnt[s] > 0: 
                n -= 1
                cnt[s] -= 1
            else:
                break
        return n