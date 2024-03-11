# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        MOD = 1<<31

        def fn(node,target1,target2):
            if node is None:
                return (-10,False,False)
            hl1,hl2,bl = fn(node.left,target1,target2)
            if bl:
                return (hl1,hl2,True)
            hr1,hr2,br = fn(node.right,target1,target2)
            if br:
                return (hr1,hr2,True)
            h1 = ((1<<3) * node.val + (1<<2) * hl1 + (1<<1) * hr1)%MOD
            h2 = ((3**3) * node.val + (3**2) * hl2 + (3**1) * hr2)%MOD
            return (h1,h2,target1==h1 and target2 == h2)
        h1,h2,_ = fn(subRoot,None,None)
        _,_,b = fn(root,h1,h2)
        return b
        