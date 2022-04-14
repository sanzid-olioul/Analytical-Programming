import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opl = ['+', '-', '*', '/']
        stk = []
        for x in tokens:
            if x not in opl:
                stk.append(x)
            else:
                m = stk.pop()
                n = stk.pop()
                tt = n + x + m
                z = eval(tt)
                stk.append(str(math.trunc(z)))
        return stk[0]