class Solution:
    def climbStairs(self, n: int) -> int:
        dict = {1:1, 2: 2}
        a = 0
        for i in range(3, n+1):
            a = dict[i-1]+dict[i-2]
            if i not in dict:
                dict[i] = a
        return dict[n]