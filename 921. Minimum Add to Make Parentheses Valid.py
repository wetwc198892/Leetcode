class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left = 0
        result = 0
        for i in S:
            if i == '(':
                left += 1
            elif i == ')':
                if left >0:
                    left -= 1
                else:
                    result += 1
        return left + result