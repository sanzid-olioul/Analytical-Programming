class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return False if num>9 and num%10 ==0 else True