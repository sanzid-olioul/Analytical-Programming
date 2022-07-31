class Solution:
    def myAtoi(self, s: str) -> int:
        num = None
        i = 0
        neg = False
        pos = False
        while i< len(s) :
            if s[i] == ' ' or s[i] =='-' or s[i] =='+' or (ord(s[i]) >= 48 and ord(s[i])<= 57):
                if s[i] == '-':
                    neg = True
                    if num != None:
                        neg = False
                        break

                if s[i] == '+':
                    pos =True
                    if num != None:
                        break
                if s[i] == ' ':
                    if num != None:
                        break
                if neg and pos:
                    return 0
                if ord(s[i]) >= 48 and ord(s[i])<= 57:
                    if num == None:
                        num = 0
                    num = num*10 + int(s[i])
                i+=1
            else:
                break
        if num == None:
            num = 0
        if neg:
            if num > 2**31:
                num =2**31
            num *=-1
        else:
            if num > 2**31-1:
                num =2**31 -1
        return num