class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in range(len(digits)):
            sum = sum*10 + digits[i]
        sum+=1
        res = []
        while sum!=0:
            res.insert(0,sum%10)
            sum//=10
        return res