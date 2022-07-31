class Solution:
    def hammingWeight(self, n: int) -> int:
        cou = 0
        while n:
            if n & 1:
                cou+=1
            n=n<<1
        return cou