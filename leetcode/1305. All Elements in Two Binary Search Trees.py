# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lst = []
        def dfs(root):
            nonlocal lst
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            lst.append(root.val)

        if root1:
            dfs(root1)
        if root2:
            dfs(root2)
        return sorted(lst)