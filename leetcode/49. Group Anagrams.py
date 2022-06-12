class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for dta in strs:
            st = tuple(sorted(list(dta)))
            res[st] = res.get(st,[])
            res[st].append(dta)
        return res.values()
