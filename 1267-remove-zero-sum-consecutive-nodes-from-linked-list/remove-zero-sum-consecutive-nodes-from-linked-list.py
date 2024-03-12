# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        5 3 1 2 -4 2 1
        """
        prefix = 0
        d = {}
        dummy = ListNode(-1,head)
        ptr = dummy.next
        d[0] = dummy
        while ptr:
            prefix += ptr.val
            if prefix not in d:
                d[prefix] = ptr
            else:
                sub_ptr = d[prefix].next
                sub_prefix = prefix
                while sub_ptr is not ptr:
                    sub_prefix+=sub_ptr.val
                    del d[sub_prefix]
                    sub_ptr = sub_ptr.next
                d[prefix].next = ptr.next
            ptr = ptr.next
        return dummy.next
            


        