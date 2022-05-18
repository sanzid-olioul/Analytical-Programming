class Solution:
    def toHex(self, num: int) -> str:
        mdict = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        rem = 0
        hexa = ""
        if num == 0:
            return str(0)
        elif num > 0:
            while num>0:
                rem = num%16
                hexa = str(mdict[rem]) + hexa
                num = num//16
        else:
            num = num + 2**32
            while num>0:
                rem = num%16
                hexa = str(mdict[rem]) + hexa
                num = num//16
                
        return hexa