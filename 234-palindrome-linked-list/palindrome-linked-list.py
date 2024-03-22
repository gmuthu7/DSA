# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ptr = head
        prev = slow
        slow = slow.next
        prev.next = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        ptr = head
        ptr2 = prev
        while ptr2:
            if ptr.val != ptr2.val:
                return False
            ptr2=ptr2.next
            ptr=ptr.next
        return True



