class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) ==0:
            return 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                flg = True
                for j in range(1,len(needle)):
                    if (i+j < len(haystack)) and (haystack[i+j] == needle[j]):
                        continue
                    else:
                        flg = False
                        break
                if flg== True:
                    return i
        return -1