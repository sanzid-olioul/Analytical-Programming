class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        lst = []
        ps = "Push"
        pp = "Pop"
        for i in range(1,n+1):
            lst.append(ps)
            if i not in target:
                lst.append(pp)
            if i == target[-1]:
                break
        return lst