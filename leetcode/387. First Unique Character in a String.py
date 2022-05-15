class Solution:
    def firstUniqChar(self, s: str) -> int:
        lst = [0 for i in range(26)]
        res = -1
        for ch in s:
            lst[ord(ch)-97]+=1
        for ind,ch in enumerate(s):
            if lst[ord(ch)-97] ==1:
                return ind

        return res
