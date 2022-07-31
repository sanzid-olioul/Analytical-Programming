class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = "{0:b}".format(x)[::-1]
        by = "{0:b}".format(y)[::-1]
        diff = 0
        for i in range(max(len(bx),len(by))):
            if len(bx) >i and len(by)>i :
                if bx[i] != by[i]:
                    diff+=1
            elif len(bx) >i:
                if bx[i] == '1':
                    diff+=1
            else:
                if by[i] == '1':
                    diff+=1
        return diff