class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)-1
        l = n//2
        for i in range(l+1):
            s[i], s[n-i] = s[n-i],s[i]