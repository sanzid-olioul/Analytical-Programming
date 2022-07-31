class Solution:
    def countBits(self, n: int) -> List[int]:                                           
        res =[0]
        for i in range(1,n+1):
            x = i
            cou = 0
            while x:
                if x & 1:
                    cou+=1
                x = x>>1
            res.append(cou)
        return res