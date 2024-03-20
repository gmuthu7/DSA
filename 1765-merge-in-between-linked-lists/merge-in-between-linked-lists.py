# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        ptr1 = list1
        b = b - a + 2
        while a > 1:
            ptr1 = ptr1.next
            a-=1
        ptr2 = ptr1
        while b > 0:
            ptr2 = ptr2.next
            b-=1
        ptr3 = list2
        while ptr3.next is not None:
            ptr3= ptr3.next
        ptr1.next = list2
        ptr3.next = ptr2
        return list1
        