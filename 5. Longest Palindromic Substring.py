class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        result = ''
        i = 0
        while n-i+1 > len(result): 
            count = 0
            for j in range(i,n):
                if s[i] == s[j] and s[i:j+1] == s[j-n:i-n-1:-1]:
                    if len(result)<len(s[i:j+1]):
                        result = s[i:j+1]
                    count = 0
                else:
                    count += 1
                if count >
            i += 1
        return result