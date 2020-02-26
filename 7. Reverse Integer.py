class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x:
            if x[0] == '-':
                x = '-' + x[len(x)-1:0:-1]
            else:
                x = x[::-1]
        x = int(x)
        if -2**31 <= x <= 2**31-1:
            return x
        else:
            return 0
        