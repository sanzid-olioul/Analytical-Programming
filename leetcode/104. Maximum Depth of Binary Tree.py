# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        def find_def(node):
            nonlocal maxdepth
            if not node:
                return 0
            l = find_def(node.left) +1
            r = find_def(node.right)+1
            maxdepth = max(l,r)
        find_def(root)
        return maxdepth

