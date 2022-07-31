# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = None
        def dfs(rt,an,tg):
            nonlocal res
            if rt == tg:
                res = an
            if not res:
                if rt.left:
                    dfs(rt.left,an.left,tg)
                if rt.right:
                    dfs(rt.right,an.right,tg)
        dfs(original,cloned,target)
        return res