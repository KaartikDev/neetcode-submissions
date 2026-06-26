# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next
            tail = tail.next

        while p1:
            tail.next = p1
            p1 = p1.next
            tail = tail.next
        
        while p2:
            tail.next = p2
            p2 = p2.next
            tail = tail.next
        
        return dummy.next