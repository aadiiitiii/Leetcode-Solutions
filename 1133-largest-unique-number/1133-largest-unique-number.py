class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return next((x for x in range(1000, -1, -1) if count[x] == 1), -1)