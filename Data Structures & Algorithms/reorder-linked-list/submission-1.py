# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #now slow is at the halfway point

        count = 0
        fast = head
        slow = head
        while fast and fast.next:
            # temp1 = slow.next
            # temp2 = fast.next.next

            slow = slow.next
            fast = fast.next.next

        #now we must reverse top half of linked list
        curr = slow.next #Slow next
        slow.next = None #cut the list
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        slow.next = None
        # print(prev.val)
        # print(head.val)
        
        
        p1 = head
        p2 = prev

        while p2:
            #save for later
            tmp1 = p1.next
            tmp2 = p2.next

            #rewire
            p1.next = p2
            p2.next = tmp1

            #inc both pointers forward
            p1 = tmp1
            p2 = tmp2
        
        
        






        


        
        
        

