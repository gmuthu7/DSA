# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def fn(node,ldepth):
            if node is None:
                return (0,True)
            if ldepth == 0:
                return (-1,False)
            l,lb = fn(node.left,ldepth-1)
            if lb:
                rdepth = min(ldepth-1,l+1)
                r,rb = fn(node.right,rdepth)
                if rb:
                    if abs(r-l) <= 1:
                        return (1 + max(l,r),True)
                    else:
                        return (-1,False)
                
            return (-1,False)
        return fn(root,10000)[1]
            
            

        