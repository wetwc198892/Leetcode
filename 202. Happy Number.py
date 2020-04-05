class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while count<6:
            strNum = str(n)
            n = 0
            for i in strNum:
                n += int(i)**2
            if n == 1:
                return True
            count += 1
        return False