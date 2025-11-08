class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap ={} #value:index hashmap

        for i, n in enumerate(nums):
            diff = target - n #difference between target and current number
            if diff in prevMap: #check if it exists
                return [prevMap[diff], i] #if it does return (location of that number,current location)
            prevMap[n] = i #else add to hashmap
        return
