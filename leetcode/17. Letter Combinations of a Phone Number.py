class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        multiplier = 0
        res = []

        for i in range(3):
            cr = ''
            for j in range(len(digits)):
                rs1 = ((int(digits[j]) -2) * 3 + i) + 97
                for k in range(len(digits)):
                    rs2 = ((int(digits[k]) -2) * 3 + i) + 97
                    
                    cr = chr(rs1) + chr(rs2)
                    res.append(cr)
                if cr == '':
                    res.append(chr(rs1))
            
        return res

