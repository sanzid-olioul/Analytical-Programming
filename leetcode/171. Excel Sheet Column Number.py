class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rct = columnTitle[::-1]
        res = 0
        i = 0
        for ch in rct:
            res += (26**i)*(ord(ch)-64)
            i+=1
        return res