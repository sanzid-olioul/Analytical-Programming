class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for stri in s:
            if ord(stri) >=65 and ord(stri) <=90:
                st+= stri.lower()
            
            if ord(stri) >=97 and ord(stri) <=122:
                st+= stri
            if ord(stri) >=48 and ord(stri) <=57:
                st+= stri
        if st == st[::-1]:
            return True
        return False