from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1=Counter(s)
        t1=Counter(t)
        for i in t1:
            if s1[i]!=t1[i]:
                return i