# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                cur.append(node.val)
            res.append(cur)
        return res
            
        