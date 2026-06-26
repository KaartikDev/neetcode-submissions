# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head):
        p = head
        prev = None
        while(p):
            next_node = p.next
            p.next = prev
            prev = p
            p = next_node

        final_head = prev
        final_tail = head
        # print(f"FINAL TAIL AFTER REVSE IS {final_tail.val}")
        return (final_head,final_tail)
        

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        dummyHead = ListNode(-1)
        dummyHead.next = head
        p = dummyHead

        #general idea: disconnect the NEXT K nodes from head and tail, reverse, then reconnect

        while p:
            curr_len = 0
            curr_head = p.next
            curr_tail = p.next
            curr = curr_head
            while curr and curr_len < k:
                curr_len+=1
                curr_tail = curr
                # print(curr.val)
                curr = curr.next
            
            if curr_len < k:
                break

            #one after end
            after_end = curr
            # print(p.val,curr_head.val, curr_tail.val,curr.val,after_end.val,)
            #disconnect curr_head and curr_tail
            p.next = None
            curr_tail.next = None
            #reverse
            (curr_head, curr_tail) = self.reverse(curr_head)
            # print(p.val,curr_head.val, curr_tail.val,curr.val,after_end.val,)
            #recconnect
            p.next = curr_head
            curr_tail.next = after_end
            #inc forward
            p = curr_tail
            # print(p.val,curr_head.val, curr_tail.val,curr.val,after_end.val,)
            

                
        
        return dummyHead.next
            


            

    