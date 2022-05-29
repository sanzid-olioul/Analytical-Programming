class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        sets = []
        for word in words:
            sets.append(set(word))
        
        maxlen = 0
        for i in range(n):
            for j in range(i+1, n):
                if len(sets[i].intersection(sets[j])) == 0:
                    maxlen = max(maxlen, len(words[i]) * len(words[j]))
        return maxlen