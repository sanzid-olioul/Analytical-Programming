class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cl = ''
        while columnNumber>0:
            if columnNumber %26 == 0:
                cl = 'Z'+ cl
                columnNumber-=26
            else:
                cl=chr(64+columnNumber%26)+cl
            columnNumber-=columnNumber%26
            columnNumber = columnNumber //26
        return cl