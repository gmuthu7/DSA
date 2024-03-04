# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        1 2 3 4 5 6
        1 6 2 5 3 4
        1 2 3 4 5 
        1 5 2 4 3
        """
        n = 0
        ptr = head
        while ptr is not None:
            n+=1
            ptr = ptr.next
        
        l = 0
        ptr = head
        prev = None
        while ptr is not None:
            if l == math.ceil(n/2.) - 1:
                temp = ptr.next
                ptr.next = None
                ptr = temp
            elif l == math.ceil(n/2.):
                prev = ptr
                ptr = ptr.next
                prev.next = None
            elif prev is not None:
                temp = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = temp
            else:
                ptr = ptr.next                
            l+=1

        ptr2 = prev
        ptr = head
        while ptr and ptr2:
            temp = ptr.next
            ptr.next = ptr2
            temp2 = ptr2.next
            ptr2.next = temp
            ptr = temp
            ptr2 = temp2
        return head


                
