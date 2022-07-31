class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n[::-1]
        
        while len(n)<32:
            n+= '0'
        sum = 0
        for i,num in enumerate(n[::-1]):
            print(i, num)
            sum+= int(num) * (2**i)
        return sum
