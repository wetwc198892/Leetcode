class Solution:
    def intToRoman(self, num: int) -> str:
        my_base = [(1000,'M'), (900,"CM"), (500,"D"), (400,"CD"), (100,"C"), (90,"XC"), (50,"L"), (40,"XL"), \
                   (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")]
        res = ''
        for n in my_base:
            if num >= n[0]:
                count = num//n[0]
                res += n[1]*count
                num -= count*n[0]
            if num == 0:
                break
        return res