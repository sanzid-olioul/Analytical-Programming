class Solution:
    def convertToBase7(self, num: int) -> str:
        rtn = ''
        if num ==0:
            return '0'
        flg = False
        if num <0:
            flg = True
            num*=-1
        while num:
            rtn = str(num %7) + rtn
            num//=7
        return '-'+rtn if flg else rtn
