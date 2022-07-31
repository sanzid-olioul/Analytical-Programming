class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        locations=[i for i in range(len(s)) if s[i]==c]
        return [min([abs(i-j)for j in locations])for i in range (len(s))]