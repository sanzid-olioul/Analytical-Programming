class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        ln = 0
        for st in s:
            if st in lst:
                if len(lst) > ln:
                    ln = len(lst)
                lst= lst[lst.index(st)+1:]
                lst.append(st)
            else:
                lst.append(st)
                if len(lst) > ln:
                    ln = len(lst)
        return ln