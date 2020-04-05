class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        for i in sorted(intervals,key=lambda x:x[0]):
            if not result:
                result.append(i)
            else:
                if result[-1][1] >= i[0]:
                    result[-1] = [result[-1][0],max(result[-1][1],i[1])]
                else:
                    result.append(i)
        return result