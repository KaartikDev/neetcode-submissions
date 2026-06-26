# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2: #both lists empty gaurd
            return list1

        curr1 = list1
        curr2 = list2

        p = ListNode() #start first node
        head = p
        if curr1 and curr2 and curr1.val < curr2.val: #both lists exist
            p.val = curr1.val
            curr1 = curr1.next
        elif curr1 and not curr2: #only l1 list exist
            p.val = curr1.val
            curr1 = curr1.next
        elif curr2 and not curr1: #only l2 exist
            p.val = curr2.val
            curr2 = curr2.next
        else: #both exist l2[0] < l1[0]
            p.val = curr2.val
            curr2 = curr2.next
        
        
        while curr1 and curr2:
            if curr1.val < curr2.val:
                p.next = ListNode(curr1.val)
                p = p.next
                curr1 = curr1.next
            else:
                p.next = ListNode(curr2.val)
                p = p.next
                curr2 = curr2.next
        
        while curr1:
            p.next = ListNode(curr1.val)
            p = p.next
            curr1 = curr1.next
        
        while curr2:
            p.next = ListNode(curr2.val)
            p = p.next
            curr2 = curr2.next
        
        return head


        
        