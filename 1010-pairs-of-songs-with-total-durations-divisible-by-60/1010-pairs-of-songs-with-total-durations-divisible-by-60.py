class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
     seen = collections.Counter()
     count = 0
     for song in time:
          count += seen[-song%60]
          seen[song % 60] += 1
     return count