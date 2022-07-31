class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ca = ord(s[0])
        cin = int(s[1])
        ra = ord(s[3])
        ri = int(s[4])
        rtn = []
        while ca <= ra:
            ci = cin
            while ci <= ri:
                vl = chr(ca) + str(ci)
                rtn.append(vl)
                ci +=1
            ca+=1
        return rtn