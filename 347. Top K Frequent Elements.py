class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in collections.Counter(nums).most_common(k):
            result.append(i[0])
        return result
      