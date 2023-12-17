# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ Method-1 : two pass algorithm"""
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # step-1: calculate the size of linked list
        sz = 0
        ptr = head
        while ptr != None:
            sz += 1
            ptr = ptr.next

        # step-2: check base condition
        if n == sz:
            return head.next

        # step-3: Initialize variables
        prev, curr, jump = None, head, sz-n

        while jump > 0:
            prev = curr
            curr = curr.next
            jump -= 1
        
        prev.next = curr.next
        return head
    
    """ Method-2 : One Pass Algorithm """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # step-1
        preleft = None
        left = right = head

        # step-2
        while n > 0:
            right = right.next
            n -= 1

        # step-3
        while right:
            preleft = left
            left = left.next
            right = right.next
        # step-4
        if preleft == None:
            return head.next

        # step 5 and 6
        preleft.next = left.next
        return head