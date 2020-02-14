class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1
        dict_trust = {}
        for i in trust:
            dict_trust.setdefault(i[0],[]).append(i[1])
        result = []
        begin = True
        for i in dict_trust.values():
            if not result:
                if begin:
                    result=i
                    begin = False
                    continue
                else:
                    return -1
            result = list(set(result) & set(i))
        if not result or len(result)>1:
            return -1
        return result[0]