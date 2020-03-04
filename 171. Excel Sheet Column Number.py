class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            result += (ord(s[i])-64)*(26**(n-i-1))
        return result