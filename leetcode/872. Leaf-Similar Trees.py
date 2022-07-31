# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def fm(rt):
            if not rt:
                return []
            elif not rt.left and not rt.right:
                return [rt.val]
            else:
                lv = fm(rt.left)
                rv= fm(rt.right)
                return lv+rv 
        lst1 = fm(root1)
        lst2 = fm(root2)
        return True if lst1 ==lst2 else False