import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.fullmatch(p, s) == None: return False
        else: return True