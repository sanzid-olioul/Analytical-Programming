class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = []
        n = len(s)
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                lst.append(s[i])
        lst = lst[::-1]
        j=0
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                s = s[:i]+ lst[j] + s[i+1:]
                j+=1
        return s


