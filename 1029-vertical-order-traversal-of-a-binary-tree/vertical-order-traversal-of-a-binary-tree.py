# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = defaultdict(list)
        res = []
        def helper(node,row,col):
            if node is None:
                return
            d[col].append((node.val,row))
            helper(node.left,row+1,col-1)
            helper(node.right,row+1,col+1)
        helper(root,0,0)
        res = []
        for key in sorted(d.keys()):
            res.append([val[0] for val in sorted(d[key],key=lambda x : (x[1],x[0]))])
        return res        