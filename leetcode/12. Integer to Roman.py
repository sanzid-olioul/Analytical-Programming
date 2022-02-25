class Solution:
    def __init__(self):
        self.dct = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        self.lst = list(self.dict)
        
    def intToRoman(self, num: int) -> str:
        rstr = ''
        while num!= 0:
            for i in range(6,-1,-1):
                if self.dct[self.lst[i]] < num:
                    rstr+= self.lst[i]
                    num-= self.dct[self.lst[i]]
                elif 
