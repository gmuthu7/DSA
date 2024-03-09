# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def fn(val,carry):
            res = val + carry
            if res>9:
                res-=10
                carry = 1
            else:
                carry = 0
            return res,carry
        carry = 0
        ptr1 = l1
        ptr2 = l2
        res = 0
        pos = 0
        prev = None
        while ptr1 is not None and ptr2 is not None:
            digit,carry = fn(ptr1.val+ptr2.val,carry)
            ptr1.val = digit
            pos+=1
            prev = ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if ptr2 is not None:
            prev.next = ptr2
        while ptr2 is not None:
            digit,carry = fn(ptr2.val,carry)
            ptr2.val = digit
            prev = ptr2
            pos+=1
            ptr2 = ptr2.next
        while ptr1 is not None:
            digit,carry = fn(ptr1.val,carry)
            ptr1.val = digit
            prev = ptr1
            res = res + digit * (10**pos)
            pos+=1
            ptr1 = ptr1.next
        if carry != 0:
            prev.next = ListNode(carry,None)
        return l1
            


                
