class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, 2**16
        if num == 1:
            return True
        while start <= end:
            mid = start + (end-start)//2
            if (mid**2) == num: return True
            elif (mid**2) > num: end = mid - 1
            elif (mid**2) < num: start = mid + 1
        return False