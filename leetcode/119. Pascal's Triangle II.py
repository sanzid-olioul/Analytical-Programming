
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fac(n):
            if n==0:
                return 1
            return n * fac(n-1)
        def ncr(n,r):
            return fac(n)//(fac(r)*fac(n-r))
        res = []
        for i in range(rowIndex+1):
            res.append(ncr(rowIndex,i))
        return res
