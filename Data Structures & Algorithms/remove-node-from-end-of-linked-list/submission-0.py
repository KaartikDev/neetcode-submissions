# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        N = 0


        while p:
            N+=1
            p = p.next
        
        
        index_to_del = N-n
        # print(index_to_del)
        
        #gaurd against delting head node
        if index_to_del == 0:
            head = head.next
            return head
        
        #deleting some other node
        i = 1
        p = head
        while p and i < index_to_del:
            p = p.next
            i+=1
        
        if index_to_del == 0:
            head = head.next
            return head

        #save
        temp = p.next
        #rewire
        if p.next:
            p.next = p.next.next
        else:
            head = None
        #detach
        if temp:
            temp.next = None

        return head

    

        