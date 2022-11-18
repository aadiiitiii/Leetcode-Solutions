class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = [str(x) for x in nums]
    
        ans = 0
        for num in nums:
            if len(num) % 2 == 0:
                ans += 1

        return ans