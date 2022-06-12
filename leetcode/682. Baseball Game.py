class Solution:
    def calPoints(self, ops: List[str]) -> int:
        lst = []
        for dt in ops:
            if dt == "D":
                lst.append(lst[-1]*2)
            elif dt == "C":
                lst.pop()
            elif dt == "+":
                res = lst[-1]+lst[-2]
                lst.append(res)
            else:
                lst.append(int(dt))
        return sum(lst)
