class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = strs[0]
        nst = ""
        f = True
        if len(strs) == 1:
            return st
        for i in range(1,len(strs)):
            if st != "" and strs[i]!="" and st[0] == strs[i][0]:
                m = min(len(st),len(strs[i]))
                for j in range(0,m):
                    if st[j] == strs[i][j]:
                        nst+=st[j]
                        f = False
                    else:
                        break
            st = nst
            nst = ""

        if f:
            return ""
        return st