# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #now slow.next is top half
        topHead = slow.next
        #disconnect bottom half
        slow.next = None

        #reverse top half
        topCurr = topHead
        topPrev = None
        while topCurr:
            temp = topCurr.next
            topCurr.next = topPrev
            topPrev = topCurr
            topCurr = temp
        
        topCurr = topPrev #reassign topCurr to prev as we revered

        #now need to merge
        bottomCurr = head
        while bottomCurr and topCurr:
            nextBottom = bottomCurr.next
            nextTop = topCurr.next

            bottomCurr.next = topCurr
            topCurr.next = nextBottom

            bottomCurr = nextBottom
            topCurr = nextTop
        
        # return head








        


        
        
        

