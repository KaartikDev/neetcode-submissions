# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # MAX_LIST_LNEGTH = 1000
        # i = 0

        # while(head and i <= MAX_LIST_LNEGTH):
        #     head = head.next
        #     i+=1
        
        # # print(i)
        # if i > 1000:
        #     return True
        # else:
        #     return False
        
        ## better sol

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
