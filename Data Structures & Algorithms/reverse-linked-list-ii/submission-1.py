# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #sol
        # iterate while checking until left-1 index
        
        #idea
        #put a dummy node on so we can be zero index and remove left at start edge

        dummyHead = ListNode(-1,head)
        index = 0
        spliceP = dummyHead

        while index < left-1:
            spliceP = spliceP.next
            index+=1
        
        #save start of reverse point
        leftP = spliceP.next
        index+=1

        #disconnect
        spliceP.next = None

        #now reverse
        prev = None
        curr = leftP
        
        temp = None
        while index <= right and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            index+=1
        
        #reconnect
        spliceP.next = prev

        leftP.next = temp

        return dummyHead.next





        
        





        
