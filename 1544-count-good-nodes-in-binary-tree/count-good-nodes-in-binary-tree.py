# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        count = 0
        stack.append((root,root.val))
        while stack:
            node,m1 = stack.pop()
            m2 = max(node.val,m1)
            if m2 == node.val:
                count+=1
            if node.left:
                stack.append((node.left,m2))
            if node.right:
                stack.append((node.right,m2))
        return count
            
        