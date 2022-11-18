class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        mx = 2**30  # 30 is the largest power of 2 inside the constraint of 2**31-1 

        return n>0 and mx%n==0