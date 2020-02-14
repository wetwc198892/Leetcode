class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort(reverse=True)
            result = stones.pop(0)-stones.pop(0)
            if(result==0):
                continue
            stones.append(result)
        if len(stones)>0:
            return stones[0]
        return 0