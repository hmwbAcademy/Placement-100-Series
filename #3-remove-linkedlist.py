# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ Method-1: Using Stack """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # write your code here
        stack = []

        while head != None:
            stack.append(head)
            head = head.next
        
        if not stack:
            return None

        head = tail = stack.pop()

        while len(stack) > 0:
            tail.next = stack.pop()
            tail = tail.next

        tail.next = None

        return head

    """ Method-2 : Iterative Approach """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev