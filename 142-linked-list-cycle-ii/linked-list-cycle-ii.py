# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        cycle_l = 0
        slow = None
        while slow is not fast:
            if not slow:
                slow = fast.next
            else:
                slow = slow.next
            cycle_l += 1
        fast = head
        while cycle_l:
            fast = fast.next
            cycle_l-=1
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return fast

        
        
        
        