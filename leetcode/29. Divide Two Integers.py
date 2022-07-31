class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flg = False
        if dividend <0 :
            flg = not flg
            dividend = int((str(dividend))[1:])
        if divisor <0:
            flg = not flg
            divisor = int((str(divisor))[1:])
        cou = 0
        if dividend ==1 and divisor ==1:
            cou+=1
        for i in range(1,dividend,divisor):
            cou+=1
        return cou if not flg else int(('-'+str(cou)))