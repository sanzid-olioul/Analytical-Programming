class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lns = len(s)
        lnt = len(t)
        i=0
        while i <lns:
            if s[i]=="#":
                if i == 0:
                    s=s[i+1:]
                    lns -=1
                    continue
                if i+1<lns:
                    s= s[:i-1]+s[i+1:]
                else:
                    s= s[:i-1]
                if lns >1:
                    lns-=2
                if i >0:
                    i-=1
            else:
                i+=1
        i=0
        while i <lnt:
            if t[i]=="#":
                if i == 0:
                    t=t[i+1:]
                    lnt-=1
                    continue
                if i+1< lnt:
                    t= t[:i-1]+t[i+1:]
                else:
                    t= t[:i-1]
                if lnt >1:
                    lnt-=2
                if i >0:
                    i-=1
            else:
                i+=1
        print(s,t)
        if s == t:
            return True
        return False