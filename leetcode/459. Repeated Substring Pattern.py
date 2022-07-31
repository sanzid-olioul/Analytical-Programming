class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        if l==1:
            return False

        i = 1
        h = l//2
        while i<=h:
            if (l-i)%i==0 and self.check(s[0:i], i, s[i:], l-i):
                return True
            i+=1
        return False

    def check(self, s1, l1, s2, l2):
        i = 0
        while i<l2:
            if i+l1<=l2 and s2[i:i+l1]==s1:
                i+=l1
            else:
                return False
        return True