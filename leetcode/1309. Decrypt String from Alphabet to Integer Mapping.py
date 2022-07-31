class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        res = []
        i = 0
        while i <n:
            if i+2 < n and s[i+2]=='#':
                res.append(int(s[i:i+2]))
                i+=3
            else:
                res.append(int(s[i]))
                i+=1
        rtn = ''
        for i in res:
            rtn+=chr(i+96)
        return rtn
            
        
