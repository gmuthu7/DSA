# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif (not p and q) or (not q and p) or (p.val != q.val):
            return False
        elif p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True