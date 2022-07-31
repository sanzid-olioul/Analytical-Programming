import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        if num == 1:
            return False
        ln = math.floor(math.sqrt(num))
        for i in range(2,ln+1):
            if num%i ==0:
                sum+= i
                sum+= num/i
        return True if sum == num else False
