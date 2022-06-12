class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cou = 0
        for ls in logs:
            if ls == "./":
                continue
            if ls == "../":
                if cou>0:
                    cou-=1
            else:
                cou+=1
        return cou

