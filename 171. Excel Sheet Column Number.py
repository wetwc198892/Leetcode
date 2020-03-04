class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        s = s[::-1]
        result = 0
        for i in range(n):
            if i == 0:
                result += ord(s[i])-64
            else:
                result += (ord(s[i])-64)*(26**i)
        return result