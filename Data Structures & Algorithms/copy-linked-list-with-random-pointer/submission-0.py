"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #empty list gaurd
        if not head:
            return None

        
        newHead = Node(head.val)
        saved = newHead
        p = head.next

        
        
        while (p):
            curr = Node(p.val,None,None)
            newHead.next = curr
            p = p.next
            newHead = curr
        
        # now figuring out random pointers 
        nodeMap = {} #of shape ORIGNAL : CORRSPONDING
        p = head
        newHead = saved
        #build the Correspond node map from orginal 
        while p:
            nodeMap[p] = newHead
            newHead = newHead.next
            p = p.next
        # print(nodeMap)

        # #now iterate 
        newHead = saved
        p = head
        while p:
            if p.random:
                newHead.random = nodeMap[p.random]
            p = p.next
            newHead = newHead.next
            
        return saved
            