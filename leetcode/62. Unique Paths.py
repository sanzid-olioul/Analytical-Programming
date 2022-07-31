class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        val = 0
        if m==0 or n == 0:
            return 0
        if m > 0 and n > 0:
            return 1+ self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        elif m >0:
            return self.uniquePaths(m-1,n)
        elif n > 0:
            return self.uniquePaths(m,n-1)

        