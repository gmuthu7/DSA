# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = [None]
        def rfn(node,h):
            if node is None:
                return None
            node2 = rfn(node.next,h)
            if node2 is not None:
                node2.next = node
            else:
                h[0] = node
            return node
        n = rfn(head,new_head)
        if n is not None:
            n.next = None
        return new_head[0]
        
        