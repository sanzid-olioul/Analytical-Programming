class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for st in s:
            if st == ')' and len(stack)>0:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(st)
            elif st == '}' and len(stack)>0:
                if stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(st)
            elif st == ']' and len(stack)>0:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(st)
            else:
                stack.append(st)
        if len(stack)>0:
            return False
        return True

# sl = Solution()
# print(sl.isValid('(}'))