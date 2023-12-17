# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """ Method-1: using hashmap """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap ={}
        while headA != None:
            hashmap[headA] = True
            headA = headA.next

        while headB != None:
            if hashmap.get(headB, False) == True:
                return headB
            headB = headB.next

        return None


    """ Method-2: Using Two Pointer Concept """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        #size of list A
        c1 = 0
        ptr1 = headA

        while ptr1 != None:
            c1 = c1 + 1
            ptr1 = ptr1.next
        


        # size of listB
        c2 = 0
        ptr1 = headB

        while ptr1 != None:
            c2 = c2 + 1
            ptr1 = ptr1.next


        ptr1 = headA
        ptr2 = headB

        positionMoved = 0
        if c1 < c2:
            positionMoved = c2 - c1
            while positionMoved > 0:
                ptr2 = ptr2.next
                positionMoved -= 1
        else:
            positionMoved = c1 - c2
            while positionMoved > 0:
                ptr1 = ptr1.next
                positionMoved -= 1

        while ptr1 != None and ptr2 != None:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return None