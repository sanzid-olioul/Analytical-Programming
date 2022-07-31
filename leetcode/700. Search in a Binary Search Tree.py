# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None
        def bst(rt,val):
            nonlocal res
            if not res:
                print(rt.val)
                if rt and rt.val == val:
                    res = rt
                elif rt and rt.val> val:
                    bst(rt.left,val)
                elif rt :
                    bst(rt.right,val)
        bst(root,val)
        return res