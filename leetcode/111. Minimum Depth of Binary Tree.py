class Solution(object):
    def minDepth(self, root):
        if root == None:
            return 0
        queue = [root]
        level = 1
        while len(queue)!=0:
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                if node.left == None and node.right == None:
                    return level
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            level += 1
        return level