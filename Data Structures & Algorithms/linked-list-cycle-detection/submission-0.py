# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        limit = 1001 #lenght of list is garunteed to be less than 1000

        i = 0
        curr = head
        while curr:
            curr = curr.next
            i+=1
            # print(curr, i)
            if i > limit:
                return True
        
        return False