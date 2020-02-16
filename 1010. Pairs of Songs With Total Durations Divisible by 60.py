class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq, res = [0]*60, 0
        for i in time:
            freq[i % 60] += 1
        for i in range(31):
            n = freq[i]
            if i == 0 or i == 30:
                res += n*(n-1)//2
            else:
                res += n * freq[60-i]
        return res
