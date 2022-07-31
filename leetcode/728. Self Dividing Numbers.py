class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            temp = i
            is_divide = True
            while temp:
                fl = temp%10
                if fl and i % fl==0:
                    temp//=10
                    continue

                is_divide = False
                break
            if is_divide:
                res.append(i)
        return res
