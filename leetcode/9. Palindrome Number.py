class Solution:
    def isPalindrome(self, x: int) -> bool:
        st = str(x)
        s = ''
        if x < 0:
            return False
        if x == 0:
            return True
        while x !=0:
            ls = x%10
            s+= str(ls)
            x//=10
        if s == st:
            return True
        return False

s = Solution()
print(s.isPalindrome(0))