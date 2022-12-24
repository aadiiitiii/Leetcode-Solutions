class Solution:
    def canAttendMeetings(self, A) -> bool:
        A.sort()
        return all([a[1] <= b[0] for a,b in zip(A, A[1:])])