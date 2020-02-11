class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ''
        if(len(num2) < len(num1)):
            num1,num2 = num2,num1
        temp = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            intnum1 = int(num1[i])
            intnum2 = int(num2[i])
            total = intnum1 + intnum2 + temp
            if total >= 10:
                total -= 10
                temp = 1
            else:
                temp = 0
            result += str(total)
        k = 0
        while temp == 1:
            if (len(num1)+k) <len(num2):
                total = temp + int(num2[len(num1)+k])
                if total >= 10:
                    total -= 10
                    temp = 1
                else:
                    temp = 0
                result += str(total)
                k += 1
            else:
                result += str(temp)
                return result[::-1]
        result += num2[len(num1)+k:]
        return result[::-1]