class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def fac(n):
            if n==0:
                return 1
            return n * fac(n-1)
        def ncr(n,r):
            return fac(n)//(fac(r)*fac(n-r))
        rtn = []
        for k in range(numRows):
            res = []
            for i in range(k+1):
                res.append(ncr(k,i))
            rtn.append(res)
        return rtn
