class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        st = sentence.split()
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(st)):
            if st[i][0] in vowel:
                st[i] = st[i] +'ma'+ 'a'*(i+1)
            else:
                st[i] = st[i][1:]+st[i][0]+'ma'+ 'a'*(i+1)
        return ' '.join(st)