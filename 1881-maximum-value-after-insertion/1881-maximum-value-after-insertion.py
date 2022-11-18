class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0]=='-':
            neg = 1
            while neg<len(n) and x>=int(n[neg]):
                neg=neg+1
        else:
            neg=0
            while neg<len(n) and x<=int(n[neg]):
                neg=neg+1
                
        ans=n[:neg] + str(x) + n[neg:]
        return ans