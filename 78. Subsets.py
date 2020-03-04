from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        for i in range(length+1):
            for j in combinations(nums,i):
                 result.append(j)
        return result
            