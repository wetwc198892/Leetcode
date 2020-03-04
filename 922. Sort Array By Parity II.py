class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        ans = [0]*len(A)
        t = 0
        for i in A:
            if i % 2 == 0:
                ans[t] = i
                t += 2
        t = 1
        for i in A:
            if i % 2 != 0:
                ans[t] = i
                t += 2
        return ans
