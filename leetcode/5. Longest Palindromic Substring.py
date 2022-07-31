class Solution:
    def longestPalindrome(self, s: str) -> str:
        ln = len(s)
        i,j,ini,inj = 0,1,0,1
        for k in range(1,ln):
            i = k
            j = k+1
            while i >=0 and j <ln:
                if i-1 >=0 and s[i-1] == s[j]:
                    i-=2
                    j+=1
                elif s[i] == s[j]:
                    i-=1
                    j+=1
                else:
                    break
            if i==k:
                continue
            else:
                i+=1
                if j -i > inj - ini:
                        inj = j
                        ini = i
        print(ini,' ',inj)
        return s[ini:inj]
