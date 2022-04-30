# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def insert(node,val):
            node.val = val
            return node
            
        def insertrec(arr,f,l,no):
            mid = (f+l)//2
            no = insert(no,arr[mid])
            if f< mid:
                no.left = TreeNode()
                insertrec(arr,f,mid -1,no.left)
            if mid< l:
                no.right = TreeNode()
                insertrec(arr,mid + 1,l,no.right)
        node = TreeNode()

        insertrec(nums,0,len(nums)-1,node)
        return node

