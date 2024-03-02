# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        n_ptr = head
        cntr = 0
        while cntr < n:
            n_ptr = n_ptr.next
            cntr+=1
        if n_ptr:
            while n_ptr.next != None:
                ptr = ptr.next
                n_ptr = n_ptr.next
            ptr.next = ptr.next.next
        else:
            head = head.next  
        return head

        