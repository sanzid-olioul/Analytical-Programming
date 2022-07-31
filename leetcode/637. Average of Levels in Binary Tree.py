# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dct = dict()
        def dfs(rt,lb = 0):
            nonlocal dct
            if rt == None:
                return
            dct[lb] = dct.get(lb,[])
            dct[lb].append(rt.val)
            dfs(rt.left,lb+1)
            dfs(rt.right,lb+1)
        dfs(root)
        res = []
        for k in dct.keys():
            res.append(sum(dct[k])/len(dct[k]))
        return res      