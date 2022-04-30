# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        fs = 0
        ls = n-1
        res = 1
        while fs <= ls:
            mid = (fs + ls)//2
            if isBadVersion(mid+1):
                ls = mid -1
                res = mid + 1
            else:
                fs = mid + 1
        return res