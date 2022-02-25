class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ln = 0
        cnt = 0
        for st in s:
            