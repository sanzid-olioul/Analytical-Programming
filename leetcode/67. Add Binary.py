class Solution:
    def addBinary(self, a: str, b: str) -> str:
        st = ""
        a=a[::-1]
        b=b[::-1]
        carry =0

        m,n = 0,0
        while m < len(a) and n < len(b):
            sum = int(a[m]) + int(b[n]) + carry
            m+=1
            n+=1
            carry = sum//2
            sum = sum % 2
            st = str(sum) + st

        while m < len(a):
            sum = int(a[m]) + carry
            m+=1
            carry = sum//2
            sum = sum % 2
            st = str(sum) + st
        
        while n < len(b):
            sum = int(b[n]) + carry
            n+=1
            carry = sum//2
            sum = sum % 2
            st = str(sum) + st
        if carry:
            st = str(carry) + st
        return st