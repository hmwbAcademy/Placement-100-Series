# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """ Method-1: hashmap """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {}
        curr = head

        while curr != None:
            if curr in hashmap:
                return curr
            hashmap[curr] = True
            curr =curr.next
        
        return None

    # Method-2: Hare Tortoise Algorithm
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = head
                break
        if fast == None or fast.next == None:
            return None

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow