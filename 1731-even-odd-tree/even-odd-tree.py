# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.appendleft(root)
        level = -1
        while queue:
            level += 1
            prev = float("inf") if level & 1 else -float("inf")
            i= len(queue)
            while i > 0:
                i-=1
                node = queue.pop()
                if node is None:
                    continue
                if (node.val & 1 or prev <= node.val) and level & 1 or not level & 1 and (not node.val & 1 or prev >= node.val):
                    return False
                prev = node.val
                queue.appendleft(node.left)
                queue.appendleft(node.right)
        return True

                    
                    


        