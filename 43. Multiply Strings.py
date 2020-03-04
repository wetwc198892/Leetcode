class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        stringtoint={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        inttostring=['0','1','2','3','4','5','6','7','8','9']
        if(len(num1)<len(num2)):
            num1,num2 = num2,num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        listnum = [0]*(len(num1)+len(num2))
        for i in range(len(num2)):
            for j in range(len(num1)):
                product = stringtoint[num2[i]]*stringtoint[num1[j]]+listnum[i+j]
                listnum[i+j] = product%10
                listnum[i+j+1] += product//10
        result = ''
        for i in listnum[::-1]:
            if i == 0 and not result:
                continue
            result += inttostring[i]
        return result