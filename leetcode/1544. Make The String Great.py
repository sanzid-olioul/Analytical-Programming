class Solution:
    def makeGood(self, s: str) -> str:
        strlen = len(s)
        i = 0
        while i< strlen -1:
            if abs(ord(s[i]) - ord(s[i+1])) == 32 :
                s = s[:i]+s[i+2:]
                if i >0:
                    i-=1
                strlen-=2
            else:
                i+=1
        return s