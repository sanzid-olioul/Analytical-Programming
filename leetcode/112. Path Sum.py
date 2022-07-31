# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        rsd = False
        def ps(nd,sum=0):
            nonlocal rsd
            if nd:
                sum+= nd.val
                if nd.left != None:
                    ps(nd.left,sum)
                
                if nd.right!= None:
                    ps(nd.right,sum)
                if nd.left == None and nd.right== None:
                    if sum== targetSum:
                        rsd = True
                
        ps(root)
        return rsd
            
