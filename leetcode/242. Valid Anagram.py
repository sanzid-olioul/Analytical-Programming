from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 =Counter(s)
        c2 =Counter(t)
        return True if c1 == c2 else False