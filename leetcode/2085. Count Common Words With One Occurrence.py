class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = {}
        d2 = {}
        for ls in words1:
            d1[ls] = d1.get(ls,0) +1
            
        for ls in words2:
            d2[ls] = d2.get(ls,0) +1

        s1 = { x for x in d1.keys() if d1[x]==1}
        s2 = { x for x in d2.keys() if d2[x]==1}

        return len(s1.intersection(s2))