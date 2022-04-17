class Solution:
    def calculate(self, s: str) -> int:
        sum = 0
        si = '+'
        sm = 0
        for x in range(len(s)):
            sm = 0
            while ord(s[x]) >=48 and ord(s[x]) <58 and x < len(s) :
                sm = sm*10 + int(s[x])
                x+=1
            if s[x] == '+':
                sum+=sm
                si = '+'
            if s[x] == '-':
                sum-=sm
                si = '-'
        if si == '+':
                sum+=sm
        if si == '-':
            sum-=sm
        return sum