class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count_zero = 0
        for i in arr:
            if i == 0:
                count_zero += 1
                if count_zero > 1:
                    return True
                continue
            if arr.count(i*2) > 0:
                return True
        return False
