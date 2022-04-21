import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qu1 = queue.Queue()
        qu2 = queue.Queue()
        qu1.put(p)
        qu2.put(q)
        while not qu1.empty() and not qu2.empty():
            x = qu1.get()
            y = qu2.get()
            if x == None or y == None:
                if (x == None and y !=None) or (y == None and x !=None):
                    return False
            elif x.val == y.val:
                qu1.put(x.left)
                qu1.put(x.right)
                qu2.put(y.left)
                qu2.put(y.right)
            else:
                return False
        
        if qu1.empty() and qu2.empty():
            return True
        else:
            return False
            