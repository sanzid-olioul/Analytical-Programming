"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        maxdepth=0
        def search(node,depth):
            nonlocal maxdepth
            if node:
                depth+=1
                if depth>maxdepth:
                    maxdepth=depth
                if node.children:
                    for child in node.children:
                        search(child,depth)
        search(root,0)
        return maxdepth