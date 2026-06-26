# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def delete_head(self,head):
        if not head:
            return
        
        
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]

        #counting total nodes
        total_node_count = 0
        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                total_node_count+=1
                temp = temp.next
        
        

        mergeHead = ListNode(-1)
        p = mergeHead
        index_of_min = -1
        

        for j in range(total_node_count):
            min_seen = float('inf')
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_seen:
                    # print(min_seen, index_of_min)
                    min_seen = lists[i].val
                    index_of_min = i
                
            # print(min_seen, index_of_min)
            next_node = ListNode(val=min_seen)
            p.next = next_node
            p = p.next
            # print(p.val)

            if lists[index_of_min]: #delete head
                temp = lists[index_of_min]
                lists[index_of_min] = lists[index_of_min].next
                temp.next = None
                # if lists[index_of_min]:
                #     print(lists[index_of_min].val)
                
        
        #
        # print(mergeHead.val)
        return mergeHead.next
            

        

        