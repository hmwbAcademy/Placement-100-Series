# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        head = tail = None

        if list1 == None:
            return list2

        if list2 == None:
            return list1

        while ptr1 != None and ptr2 != None:
            if ptr1.val <= ptr2.val:
                if head == None:
                    head = tail = ptr1
                else:
                    tail.next = ptr1
                    tail = tail.next
                ptr1 = ptr1.next
            else:
                if head == None:
                    head = tail = ptr2
                else:
                    tail.next = ptr2
                    tail = tail.next
                ptr2 = ptr2.next

        if ptr1 != None:
            tail.next = ptr1

        if ptr2 != None:
            tail.next = ptr2

        return head

