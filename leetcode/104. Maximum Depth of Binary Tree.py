# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find_def(node):
            if node == None:
                return 0
            
            
            l = find_def(node.left) +1
            r = find_def(node.right)+1
            maxdepth = max(l,r)
            return maxdepth
        
        return find_def(root)

