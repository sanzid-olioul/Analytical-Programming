class Solution:
    def findComplement(self, num: int) -> int:
        bin = "{0:b}".format(int(num))
        rtn = ""
        for i in bin:
            if i == '0':
                rtn+= '1'
            else:
                rtn+= '0'
        return int(rtn,2)