class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        s=0
        nums.append(0)
        for i in range(0,len(nums)):
            if nums[i] == 1:
                s+=1
            else:
                res.append(s)
                s=0
        return max(res)