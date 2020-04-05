class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        counter = collections.Counter(words)
        for value in sorted(counter.items(), key = lambda x: (-x[1],x[0])):
            result.append(value[0])
            if len(result) == k:
                break
        return result