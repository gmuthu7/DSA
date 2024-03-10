# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]
        def fn(node):
            if node is None:
                return 0
            l = fn(node.left)
            r = fn(node.right)
            longest[0] = max(longest[0],l+r)
            return 1 + max(l,r)
        fn(root)
        return longest[0]
            

        