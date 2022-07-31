# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dct = {}
        def fm(rt):
            nonlocal dct
            if rt==None:
                return
            dct[rt.val] = dct.get(rt.val,0)
            dct[rt.val]+=1
            fm(rt.left)
            fm(rt.right)
        fm(root)
        mx = max(dct,key=dct.get)
        res = []
        for k,v in dct.items():
            if v==dct[mx]:
                res.append(k)
        return res