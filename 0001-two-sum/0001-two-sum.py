class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashval = {}
        for i, n in enumerate(nums):
            diff= target-n
            if diff in hashval:
                return [hashval[diff], i]
            hashval[n]=i