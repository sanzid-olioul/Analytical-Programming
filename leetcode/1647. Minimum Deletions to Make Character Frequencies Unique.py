class Solution:
    def minDeletions(self, s: str) -> int:
        dct = {}
        for ch in s:
            dct[ch] = dct.get(ch,0)
            dct[ch]+=1
        
        lst = sorted(dct.values(),reverse=True)
        cou =0
        for i in range(1,len(lst)):
            if lst[i-1] <= lst[i]:
                if lst[i-1] == 0:
                    diff = lst[i]
                else:
                    diff= lst[i]- lst[i-1]+1
                cou+=diff
                lst[i]-=diff
        return cou