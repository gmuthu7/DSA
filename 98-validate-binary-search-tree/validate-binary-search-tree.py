# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node,lb,ub):
            if node is None:
                return True
            if node.val >= ub or node.val <= lb:
                return False
            return helper(node.left,lb,node.val) and helper(node.right,node.val,ub)
        return helper(root,float("-inf"),float("inf"))
        