class Solution:
    def __init__(self) -> None:
        self.dct = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
    def romanToInt(self, s: str) -> int:
        val = self.dct[s[0]]
        for i in range(1,len(s)):
            if self.dct[s[i-1]] >= self.dct[s[i]]:
                val+=self.dct[s[i]]
            else:
                val+=self.dct[s[i]]
                val-=2*self.dct[s[i-1]]

        return val
