class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l_val = 0
        total = 0
        res = float("inf")
        
        for r_val in range(len(nums)):
            total = total + nums[r_val]
            
            while total >= target:
                res = min(r_val-l_val+1, res)
                total = total - nums[l_val]
                l_val = l_val+1
                
        return 0 if res==float("inf") else res