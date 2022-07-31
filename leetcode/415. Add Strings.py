class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = max(len(num1),len(num2))
        
        a = num1.zfill(m)
        
        b = num2.zfill(m)
        print(a, b)
        res = ''
        carry = 0
        
        for i in range(m-1 , -1 , -1):
            upper = ord(a[i]) - ord("0")
            lower = ord(b[i]) - ord("0")
            
            res += str((carry + upper + lower) % 10)
            
            carry = (upper + lower+carry) // 10 
        if carry == 1:
            res += str(carry) 
        return res[::-1]