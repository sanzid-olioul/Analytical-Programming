class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root==None:
                return 0
            left=height(root.left)
            right=height(root.right)
            if left==-1 or right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return False if height(root)==-1 else True