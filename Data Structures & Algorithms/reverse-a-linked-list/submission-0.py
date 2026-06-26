# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: #empty/single node gaurd
            return head

        curr = head
        nextNode = None
        prev = None

        while curr:
            nextNode = curr.next #Reassign nextNode pointer to the next node

            curr.next = prev #break the link of current to future and move it to past

            prev = curr #update the previous to current
            curr = nextNode#update the current to next node

        head = prev #start at the very end of the list
        return prev