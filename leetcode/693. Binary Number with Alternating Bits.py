class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bt = bin(n)[2:]
        for i in range(len(bt)-1):
            if bt[i]==bt[i+1]:
                return False
        return True