# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return self.arr
        if root.left != None:
            self.inorderTraversal(root.left)
        self.arr.append(root.val)
        # print(root.val)
        if root.right != None:
            self.inorderTraversal(root.right)
        return self.arr