class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        arr = [0 for x in range(26)]
        for x in s:
            arr[ord(x)-97] +=1
        st = ""
        for i in range(26):
            if(arr[i]>0):
                st+=chr(i+97)
        return st