class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return list(str((int(''.join(str(i) for i in A))+K)))