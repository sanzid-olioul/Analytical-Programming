# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        lst = []
        def tree_traverse(rt):
            nonlocal lst
            lst.append(rt)
            if rt.left:
                tree_traverse(rt.left)
            if rt.right:
                tree_traverse(rt.right)
            
        return lst