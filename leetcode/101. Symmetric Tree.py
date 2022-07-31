class Solution(object):
    def isSymmetric(self, root):
        q = collections.deque([root])
        
        while q:
            level = []
            
            size =len(q)
            
            for i in range(size):
                node = q.popleft()
                if not node:
                    level.append(None)
                else:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level != level[::-1]: return False 
        
        return True