# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def fn(node,level):
            if node is None:
                return (None,-1)
            l = fn(node.left,level+1)
            r = fn(node.right,level+1)
            if l[1] < level and r[1] < level:
                return (node.val,level)
            elif l[1] == r[1]:
                return l
            else:
                return max(l,r,key=lambda x: x[1])
        return fn(root,0)[0]


            